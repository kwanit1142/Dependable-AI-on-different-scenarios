# -*- coding: utf-8 -*-
"""B19EE046_DAI_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m0WtnBSXkEWF4QCueE1PB7Gc1kKmK7BI
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install pytorch_lightning
import os
import torch
from torch.utils.data import Dataset, random_split, DataLoader
import pytorch_lightning as pl
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import numpy as np
import matplotlib.pyplot as plt
from torchvision import models
import PIL
from tqdm import tqdm
import cv2
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, balanced_accuracy_score

class ResNext(pl.LightningModule):

  def __init__(self, model_variant, num_classes):
    super().__init__()
    self.model_variant = model_variant
    if self.model_variant=='50_32x4d':
      self.model = models.resnext50_32x4d(weights=None)
      self.features = self.model.fc.in_features 
      self.model.fc = nn.Linear(self.features,num_classes)
    if self.model_variant=='101_32x8d':
      self.model = models.resnext101_32x8d(weights=None)
      self.features = self.model.fc.in_features
      self.model.fc = nn.Linear(self.features,num_classes)
    if self.model_variant=='101_64x4d':
      self.model = models.resnext101_64x4d(weights=None)
      self.features = self.model.fc.in_features
      self.model.fc = nn.Linear(self.features,num_classes)
    self.loss = nn.CrossEntropyLoss()

  def forward(self, x):
    return self.model(x)

  def training_step(self, batch, batch_no):
    x, y = batch
    logits = self(x)
    loss = self.loss(logits, y)
    return loss

  def configure_optimizers(self):
    return torch.optim.SGD(self.parameters(), weight_decay=0.0001, momentum=0.9, lr=0.1)

class ResNext_Model(pl.LightningModule):

  def __init__(self, model_variant, num_classes, w1=1, w2=0):
    super().__init__()
    self.model_variant = model_variant
    self.w1 = w1
    self.w2 = w2
    if self.model_variant=='50_32x4d':
      self.model = models.resnext50_32x4d(weights=None)
      self.features = self.model.fc.in_features 
      self.model.fc = nn.Linear(self.features,num_classes)
    if self.model_variant=='101_32x8d':
      self.model = models.resnext101_32x8d(weights=None)
      self.features = self.model.fc.in_features
      self.model.fc = nn.Linear(self.features,num_classes)
    if self.model_variant=='101_64x4d':
      self.model = models.resnext101_64x4d(weights=None)
      self.features = self.model.fc.in_features
      self.model.fc = nn.Linear(self.features,num_classes)
    self.reconstruct_layer = nn.Linear(self.features,3072)
    self.loss = nn.CrossEntropyLoss()
    self.reconstruct = nn.MSELoss()

  def forward(self, x):
    return self.model(x)

  def training_step(self, batch, batch_no):
    x, y = batch
    logits = self(x)
    loss1 = self.loss(logits, y)
    reconstruct_matrix = x
    for name, layer in self.model.named_children():
      if name=='fc':
        reconstruct_matrix = self.reconstruct_layer(reconstruct_matrix.reshape(reconstruct_matrix.shape[0],self.features))
        break
      else:
        reconstruct_matrix = layer(reconstruct_matrix)
    loss2 = self.reconstruct(reconstruct_matrix, x.reshape(x.shape[0],-1))
    total = self.w1*loss1+self.w2*loss2
    return total

  def configure_optimizers(self):
    return torch.optim.SGD(self.parameters(), weight_decay=0.0001, momentum=0.9, lr=0.1)

def transform_fn(img, mode='Train', resize=False):
  if resize==True:
    img = img.resize((224,224))
  tensor = transforms.ToTensor()(img)
  return tensor

def data_driven_transform_fn1(img, mode='Train', resize=False):
  if resize==True:
    img = img.resize((224,224))
  tensor = transforms.ToTensor()(img)
  tensor = transforms.RandomAdjustSharpness(sharpness_factor=2,p=0.5)(tensor)
  return tensor

def data_driven_transform_fn2(img, mode='Train', resize=False):
  if resize==True:
    img = img.resize((224,224))
  tensor = transforms.ToTensor()(img)
  tensor = transforms.RandomAutocontrast(p=0.5)(tensor)
  return tensor

def data_driven_transform_fn3(img, mode='Train', resize=False):
  if resize==True:
    img = img.resize((224,224))
  tensor = transforms.ToTensor()(img)
  tensor = transforms.RandomAdjustSharpness(sharpness_factor=2,p=0.5)(tensor)
  tensor = transforms.RandomAutocontrast(p=0.5)(tensor)
  return tensor

def model_return(ckpt_path, model_obj):
  ckpt = torch.load(ckpt_path)
  model_obj.load_state_dict(ckpt['state_dict'])
  return model_obj.eval().cuda()

def detect(test_loader, model_class):
  pred = []
  true = []
  for i,j in tqdm(test_loader):
    i,j = i.cuda(), j.cuda()
    prob = model_class(i)
    out = prob.max(1, keepdim=True)[1]
    pred.append(out.detach().cpu().item())
    true.append(j.detach().cpu().item())
  print(classification_report(true,pred))
  cm = confusion_matrix(true, pred)
  num_samples = np.sum(cm)
  num_samples_per_class = np.sum(cm, axis=1)
  tpr_per_class = np.diag(cm) / num_samples_per_class
  fpr_per_class = np.array(np.sum(cm, axis=0) - np.diag(cm),dtype='float64')
  fpr_per_class /= (num_samples - num_samples_per_class)
  ppv_per_class = np.diag(cm) / np.sum(cm, axis=0)
  npv_per_class = np.zeros_like(tpr_per_class)
  for i in range(len(npv_per_class)):
    idx = np.arange(len(npv_per_class)) != i
    tn = np.sum(cm[np.ix_(idx, idx)])
    fp = np.sum(cm[idx, i])
    npv_per_class[i] = tn / (tn + fp)
  macro_tpr = np.mean(tpr_per_class)
  macro_fpr = np.mean(fpr_per_class)
  macro_ppv = np.mean(ppv_per_class)
  macro_npv = np.mean(npv_per_class)
  micro_tpr = np.sum(np.diag(cm)) / num_samples
  micro_fpr = np.sum(fpr_per_class * num_samples_per_class) / num_samples
  micro_ppv = np.sum(np.diag(cm)) / np.sum(cm)
  micro_npv = np.sum(np.diag(cm)) / np.sum(cm)
  print("TPR_PER_CLASS = ",tpr_per_class)
  print("FPR_PER_CLASS = ",fpr_per_class)
  print("PPV_PER_CLASS = ",ppv_per_class)
  print("NPV_PER_CLASS = ",npv_per_class)
  print("MACRO_TPR = ",macro_tpr)
  print("MACRO_FPR = ",macro_fpr)
  print("MACRO_PPV = ",macro_ppv)
  print("MACRO_NPV = ",macro_npv)
  print("MICRO_TPR = ",micro_tpr)
  print("MICRO_FPR = ",micro_fpr)
  print("MICRO_PPV = ",micro_ppv)
  print("MICRO_NPV = ",micro_npv)

def calculate_tpr_fpr(cm, positive_label):
    tp = cm[positive_label, positive_label]
    fn = np.sum(cm[positive_label, :]) - tp
    fp = np.sum(cm[:, positive_label]) - tp
    tn = np.sum(cm) - tp - fn - fp
    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)
    return tpr, fpr

def Equalize_Odds_detect(model_class, protected_attr):
  dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform_fn)
  if protected_attr=='pet_animal':
    pet_indices = [i for i in range(len(dataset)) if dataset.targets[i] ==2 or dataset.targets[i] == 3 or dataset.targets[i] == 5 or dataset.targets[i] == 7]
    non_pet_indices = [i for i in range(len(dataset)) if dataset.targets[i] == 4 or dataset.targets[i] == 6]
    protected_indices = pet_indices if protected_attr == 'pet_animal' else non_pet_indices
    non_protected_indices = non_pet_indices if protected_attr == 'pet_animal' else pet_indices
  protected_dataset = torch.utils.data.Subset(dataset, protected_indices)
  non_protected_dataset = torch.utils.data.Subset(dataset, non_protected_indices)
  protected_dataloader = torch.utils.data.DataLoader(protected_dataset, batch_size=1, shuffle=False)
  non_protected_dataloader = torch.utils.data.DataLoader(non_protected_dataset, batch_size=1, shuffle=False)
  conf_matrices = []
  tpr_protected = []
  fpr_protected = []
  tpr_non_protected = []
  fpr_non_protected = []
  t = []
  for dataloader in [protected_dataloader, non_protected_dataloader]:
    pred = []
    true = []
    correct = 0
    total = 0
    for images, labels in tqdm(dataloader):
      images, labels = images.cuda(), labels.cuda()
      outputs = model_class(images)
      _, predicted = torch.max(outputs.data, 1)
      pred.append(predicted.detach().cpu().item())
      true.append(labels.detach().cpu().item())   
      total+=1 
    print(classification_report(true, pred))
    conf_matrices.append(confusion_matrix(true, pred))
  for class_ind in range(10):
    tpr_protected_i, fpr_protected_i = calculate_tpr_fpr(conf_matrices[0], class_ind)
    tpr_non_protected_i, fpr_non_protected_i = calculate_tpr_fpr(conf_matrices[1], class_ind)
    tpr_protected.append(tpr_protected_i)
    fpr_protected.append(fpr_protected_i)
    tpr_non_protected.append(tpr_non_protected_i)
    fpr_non_protected.append(fpr_non_protected_i)
  tpr_protected = np.nan_to_num(np.array(tpr_protected),nan=0.0)
  tpr_non_protected = np.nan_to_num(np.array(tpr_non_protected),nan=0.0)
  fpr_protected = np.nan_to_num(np.array(fpr_protected),nan=0.0)
  fpr_non_protected = np.nan_to_num(np.array(fpr_non_protected),nan=0.0)
  delta_tpr = tpr_protected - tpr_non_protected
  delta_fpr = fpr_protected - fpr_non_protected
  avg_delta_tpr_fpr = np.mean([delta_tpr, delta_fpr], axis=0)
  thresholds = avg_delta_tpr_fpr / 2
  cm_protected_thresh = np.zeros_like(conf_matrices[0])
  cm_non_protected_thresh = np.zeros_like(conf_matrices[1])
  for i in range(10):
    for j in range(10):
      if i == j:
        cm_protected_thresh[i, j] = conf_matrices[0][i, j] if tpr_protected[i] > thresholds[i] else 0
        cm_non_protected_thresh[i, j] = conf_matrices[1][i, j] if tpr_non_protected[i] > thresholds[i] else 0
      else:
        cm_protected_thresh[i, j] = conf_matrices[0][i, j] if fpr_protected[i] < thresholds[i] else 0
        cm_non_protected_thresh[i, j] = conf_matrices[1][i, j] if fpr_non_protected[i] < thresholds[i] else 0
  print("Confusion Matrix before Equality Odds Difference for Protected Groups",conf_matrices[0])
  print("Confusion Matrix before Equality Odds Difference for Non-Protected Groups",conf_matrices[1])
  print("Confusion Matrix after Equality Odds Difference for Protected Groups",cm_protected_thresh)
  print("Confusion Matrix after Equality Odds Difference for Non-Protected Groups",cm_non_protected_thresh)
  print(" ")
  
  num_samples = np.sum(conf_matrices[0])
  num_samples_per_class = np.sum(conf_matrices[0], axis=1)
  tpr_per_class = np.diag(conf_matrices[0]) / num_samples_per_class
  fpr_per_class = np.array(np.sum(conf_matrices[0], axis=0) - np.diag(conf_matrices[0]),dtype='float64')
  fpr_per_class /= (num_samples - num_samples_per_class)
  ppv_per_class = np.diag(conf_matrices[0]) / np.sum(conf_matrices[0], axis=0)
  npv_per_class = np.zeros_like(tpr_per_class)
  for i in range(len(npv_per_class)):
    idx = np.arange(len(npv_per_class)) != i
    tn = np.sum(conf_matrices[0][np.ix_(idx, idx)])
    fp = np.sum(conf_matrices[0][idx, i])
    npv_per_class[i] = tn / (tn + fp)
  macro_tpr = np.mean(tpr_per_class)
  macro_fpr = np.mean(fpr_per_class)
  macro_ppv = np.mean(ppv_per_class)
  macro_npv = np.mean(npv_per_class)
  micro_tpr = np.sum(np.diag(conf_matrices[0])) / num_samples
  micro_fpr = np.sum(fpr_per_class * num_samples_per_class) / num_samples
  micro_ppv = np.sum(np.diag(conf_matrices[0])) / np.sum(conf_matrices[0])
  micro_npv = np.sum(np.diag(conf_matrices[0])) / np.sum(conf_matrices[0])
  print("TPR_PER_CLASS before Equality Odds Difference for Protected Groups = ",tpr_per_class)
  print("FPR_PER_CLASS before Equality Odds Difference for Protected Groups = ",fpr_per_class)
  print("PPV_PER_CLASS before Equality Odds Difference for Protected Groups = ",ppv_per_class)
  print("NPV_PER_CLASS before Equality Odds Difference for Protected Groups = ",npv_per_class)
  print("MACRO_TPR before Equality Odds Difference for Protected Groups = ",macro_tpr)
  print("MACRO_FPR before Equality Odds Difference for Protected Groups = ",macro_fpr)
  print("MACRO_PPV before Equality Odds Difference for Protected Groups = ",macro_ppv)
  print("MACRO_NPV before Equality Odds Difference for Protected Groups = ",macro_npv)
  print("MICRO_TPR before Equality Odds Difference for Protected Groups = ",micro_tpr)
  print("MICRO_FPR before Equality Odds Difference for Protected Groups = ",micro_fpr)
  print("MICRO_PPV before Equality Odds Difference for Protected Groups = ",micro_ppv)
  print("MICRO_NPV before Equality Odds Difference for Protected Groups = ",micro_npv)
  print(" ")
  num_samples = np.sum(conf_matrices[1])
  num_samples_per_class = np.sum(conf_matrices[1], axis=1)
  tpr_per_class = np.diag(conf_matrices[1]) / num_samples_per_class
  fpr_per_class = np.array(np.sum(conf_matrices[1], axis=0) - np.diag(conf_matrices[1]),dtype='float64')
  fpr_per_class /= (num_samples - num_samples_per_class)
  ppv_per_class = np.diag(conf_matrices[1]) / np.sum(conf_matrices[1], axis=0)
  npv_per_class = np.zeros_like(tpr_per_class)
  for i in range(len(npv_per_class)):
    idx = np.arange(len(npv_per_class)) != i
    tn = np.sum(conf_matrices[1][np.ix_(idx, idx)])
    fp = np.sum(conf_matrices[1][idx, i])
    npv_per_class[i] = tn / (tn + fp)
  macro_tpr = np.mean(tpr_per_class)
  macro_fpr = np.mean(fpr_per_class)
  macro_ppv = np.mean(ppv_per_class)
  macro_npv = np.mean(npv_per_class)
  micro_tpr = np.sum(np.diag(conf_matrices[1])) / num_samples
  micro_fpr = np.sum(fpr_per_class * num_samples_per_class) / num_samples
  micro_ppv = np.sum(np.diag(conf_matrices[1])) / np.sum(conf_matrices[1])
  micro_npv = np.sum(np.diag(conf_matrices[1])) / np.sum(conf_matrices[1])
  print("TPR_PER_CLASS before Equality Odds Difference for Non-Protected Groups = ",tpr_per_class)
  print("FPR_PER_CLASS before Equality Odds Difference for Non-Protected Groups = ",fpr_per_class)
  print("PPV_PER_CLASS before Equality Odds Difference for Non-Protected Groups = ",ppv_per_class)
  print("NPV_PER_CLASS before Equality Odds Difference for Non-Protected Groups = ",npv_per_class)
  print("MACRO_TPR before Equality Odds Difference for Non-Protected Groups = ",macro_tpr)
  print("MACRO_FPR before Equality Odds Difference for Non-Protected Groups = ",macro_fpr)
  print("MACRO_PPV before Equality Odds Difference for Non-Protected Groups = ",macro_ppv)
  print("MACRO_NPV before Equality Odds Difference for Non-Protected Groups = ",macro_npv)
  print("MICRO_TPR before Equality Odds Difference for Non-Protected Groups = ",micro_tpr)
  print("MICRO_FPR before Equality Odds Difference for Non-Protected Groups = ",micro_fpr)
  print("MICRO_PPV before Equality Odds Difference for Non-Protected Groups = ",micro_ppv)
  print("MICRO_NPV before Equality Odds Difference for Non-Protected Groups = ",micro_npv)
  print(" ")
  num_samples = np.sum(cm_protected_thresh)
  num_samples_per_class = np.sum(cm_protected_thresh, axis=1)
  tpr_per_class = np.diag(cm_protected_thresh) / num_samples_per_class
  fpr_per_class = np.array(np.sum(cm_protected_thresh, axis=0) - np.diag(cm_protected_thresh),dtype='float64')
  fpr_per_class /= (num_samples - num_samples_per_class)
  ppv_per_class = np.diag(cm_protected_thresh) / np.sum(cm_protected_thresh, axis=0)
  npv_per_class = np.zeros_like(tpr_per_class)
  for i in range(len(npv_per_class)):
    idx = np.arange(len(npv_per_class)) != i
    tn = np.sum(cm_protected_thresh[np.ix_(idx, idx)])
    fp = np.sum(cm_protected_thresh[idx, i])
    npv_per_class[i] = tn / (tn + fp)
  macro_tpr = np.mean(tpr_per_class)
  macro_fpr = np.mean(fpr_per_class)
  macro_ppv = np.mean(ppv_per_class)
  macro_npv = np.mean(npv_per_class)
  micro_tpr = np.sum(np.diag(cm_protected_thresh)) / num_samples
  micro_fpr = np.sum(fpr_per_class * num_samples_per_class) / num_samples
  micro_ppv = np.sum(np.diag(cm_protected_thresh)) / np.sum(cm_protected_thresh)
  micro_npv = np.sum(np.diag(cm_protected_thresh)) / np.sum(cm_protected_thresh)
  print("TPR_PER_CLASS after Equality Odds Difference for Protected Groups = ",tpr_per_class)
  print("FPR_PER_CLASS after Equality Odds Difference for Protected Groups = ",fpr_per_class)
  print("PPV_PER_CLASS after Equality Odds Difference for Protected Groups = ",ppv_per_class)
  print("NPV_PER_CLASS after Equality Odds Difference for Protected Groups = ",npv_per_class)
  print("MACRO_TPR after Equality Odds Difference for Protected Groups = ",macro_tpr)
  print("MACRO_FPR after Equality Odds Difference for Protected Groups = ",macro_fpr)
  print("MACRO_PPV after Equality Odds Difference for Protected Groups = ",macro_ppv)
  print("MACRO_NPV after Equality Odds Difference for Protected Groups = ",macro_npv)
  print("MICRO_TPR after Equality Odds Difference for Protected Groups = ",micro_tpr)
  print("MICRO_FPR after Equality Odds Difference for Protected Groups = ",micro_fpr)
  print("MICRO_PPV after Equality Odds Difference for Protected Groups = ",micro_ppv)
  print("MICRO_NPV after Equality Odds Difference for Protected Groups = ",micro_npv)
  print(" ")
  num_samples = np.sum(cm_non_protected_thresh)
  num_samples_per_class = np.sum(cm_non_protected_thresh, axis=1)
  tpr_per_class = np.diag(cm_non_protected_thresh) / num_samples_per_class
  fpr_per_class = np.array(np.sum(cm_non_protected_thresh, axis=0) - np.diag(cm_non_protected_thresh),dtype='float64')
  fpr_per_class /= (num_samples - num_samples_per_class)
  ppv_per_class = np.diag(cm_non_protected_thresh) / np.sum(cm_non_protected_thresh, axis=0)
  npv_per_class = np.zeros_like(tpr_per_class)
  for i in range(len(npv_per_class)):
    idx = np.arange(len(npv_per_class)) != i
    tn = np.sum(cm_non_protected_thresh[np.ix_(idx, idx)])
    fp = np.sum(cm_non_protected_thresh[idx, i])
    npv_per_class[i] = tn / (tn + fp)
  macro_tpr = np.mean(tpr_per_class)
  macro_fpr = np.mean(fpr_per_class)
  macro_ppv = np.mean(ppv_per_class)
  macro_npv = np.mean(npv_per_class)
  micro_tpr = np.sum(np.diag(cm_non_protected_thresh)) / num_samples
  micro_fpr = np.sum(fpr_per_class * num_samples_per_class) / num_samples
  micro_ppv = np.sum(np.diag(cm_non_protected_thresh)) / np.sum(cm_non_protected_thresh)
  micro_npv = np.sum(np.diag(cm_non_protected_thresh)) / np.sum(cm_non_protected_thresh)
  print("TPR_PER_CLASS after Equality Odds Difference for Non-Protected Groups = ",tpr_per_class)
  print("FPR_PER_CLASS after Equality Odds Difference for Non-Protected Groups = ",fpr_per_class)
  print("PPV_PER_CLASS after Equality Odds Difference for Non-Protected Groups = ",ppv_per_class)
  print("NPV_PER_CLASS after Equality Odds Difference for Non-Protected Groups = ",npv_per_class)
  print("MACRO_TPR after Equality Odds Difference for Non-Protected Groups = ",macro_tpr)
  print("MACRO_FPR after Equality Odds Difference for Non-Protected Groups = ",macro_fpr)
  print("MACRO_PPV after Equality Odds Difference for Non-Protected Groups = ",macro_ppv)
  print("MACRO_NPV after Equality Odds Difference for Non-Protected Groups = ",macro_npv)
  print("MICRO_TPR after Equality Odds Difference for Non-Protected Groups = ",micro_tpr)
  print("MICRO_FPR after Equality Odds Difference for Non-Protected Groups = ",micro_fpr)
  print("MICRO_PPV after Equality Odds Difference for Non-Protected Groups = ",micro_ppv)
  print("MICRO_NPV after Equality Odds Difference for Non-Protected Groups = ",micro_npv)

"""#CIFAR-10 (Reproducing the Results)"""

train_CIFAR10 = torch.utils.data.DataLoader(dataset=datasets.CIFAR10('../data', train=True, download=True, transform=transform_fn),batch_size=256, shuffle=True, pin_memory=True, num_workers=2)
test_CIFAR10 = torch.utils.data.DataLoader(dataset=datasets.CIFAR10('../data', train=False, download=True, transform=transform_fn),batch_size=1, shuffle=True)

Model_50_32x4d = ResNext(model_variant='50_32x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/50_32x4d', benchmark=True)
trainer.fit(Model_50_32x4d, train_CIFAR10)
del trainer, Model_50_32x4d

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/50_32x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='50_32x4d',num_classes=10))
detect(test_CIFAR10, Model_50_32x4d)
del Model_50_32x4d

Model_101_32x8d = ResNext(model_variant='101_32x8d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/101_32x8d', benchmark=True)
trainer.fit(Model_101_32x8d, train_CIFAR10)
del trainer, Model_101_32x8d

Model_101_32x8d = model_return('/content/drive/MyDrive/DAI_Assignment_2/101_32x8d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_32x8d',num_classes=10))
detect(test_CIFAR10, Model_101_32x8d)
del Model_101_32x8d

Model_101_64x4d = ResNext(model_variant='101_64x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/101_64x4d', benchmark=True)
trainer.fit(Model_101_64x4d, train_CIFAR10)
del trainer, Model_101_64x4d

Model_101_64x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/101_64x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_64x4d',num_classes=10))
detect(test_CIFAR10, Model_101_64x4d)
del Model_101_64x4d

"""# CIFAR-10 with Equalized-Odds, a Post-Processing based Bias Mitigation Technique"""

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/50_32x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='50_32x4d',num_classes=10))
Equalize_Odds_detect(Model_50_32x4d, 'pet_animal')
del Model_50_32x4d

Model_101_32x8d = model_return('/content/drive/MyDrive/DAI_Assignment_2/101_32x8d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_32x8d',num_classes=10))
Equalize_Odds_detect(Model_101_32x8d, 'pet_animal')
del Model_101_32x8d

Model_101_64x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/101_64x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_64x4d',num_classes=10))
Equalize_Odds_detect(Model_101_64x4d, 'pet_animal')
del Model_101_64x4d

"""#CIFAR-10 with Data Preprocessing (3 types)

## Random Sharpness
"""

train_CIFAR101 = torch.utils.data.DataLoader(dataset=datasets.CIFAR10('../data', train=True, download=True, transform=data_driven_transform_fn1),batch_size=256, shuffle=True, pin_memory=True, num_workers=2)

Model_50_32x4d = ResNext(model_variant='50_32x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data_50_32x4d', benchmark=True)
trainer.fit(Model_50_32x4d, train_CIFAR101)
del trainer, Model_50_32x4d

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data_50_32x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='50_32x4d',num_classes=10))
detect(test_CIFAR10, Model_50_32x4d)
del Model_50_32x4d

Model_101_32x8d = ResNext(model_variant='101_32x8d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data_101_32x8d', benchmark=True)
trainer.fit(Model_101_32x8d, train_CIFAR101)
del trainer, Model_101_32x8d

Model_101_32x8d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data_101_32x8d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_32x8d',num_classes=10))
detect(test_CIFAR10, Model_101_32x8d)
del Model_101_32x8d

Model_101_64x4d = ResNext(model_variant='101_64x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data_101_64x4d', benchmark=True)
trainer.fit(Model_101_64x4d, train_CIFAR101)
del trainer, Model_101_64x4d

Model_101_64x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data_101_64x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_64x4d',num_classes=10))
detect(test_CIFAR10, Model_101_64x4d)
del Model_101_64x4d

"""## Random AutoContrast"""

train_CIFAR102 = torch.utils.data.DataLoader(dataset=datasets.CIFAR10('../data', train=True, download=True, transform=data_driven_transform_fn2),batch_size=256, shuffle=True, pin_memory=True, num_workers=2)

Model_50_32x4d = ResNext(model_variant='50_32x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data2_50_32x4d', benchmark=True)
trainer.fit(Model_50_32x4d, train_CIFAR102)
del trainer, Model_50_32x4d

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data2_50_32x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='50_32x4d',num_classes=10))
detect(test_CIFAR10, Model_50_32x4d)
del Model_50_32x4d

Model_101_32x8d = ResNext(model_variant='101_32x8d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data2_101_32x8d', benchmark=True)
trainer.fit(Model_101_32x8d, train_CIFAR102)
del trainer, Model_101_32x8d

Model_101_32x8d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data2_101_32x8d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_32x8d',num_classes=10))
detect(test_CIFAR10, Model_101_32x8d)
del Model_101_32x8d

Model_101_64x4d = ResNext(model_variant='101_64x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data2_101_64x4d', benchmark=True)
trainer.fit(Model_101_64x4d, train_CIFAR102)
del trainer, Model_101_64x4d

Model_101_64x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data2_101_64x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_64x4d',num_classes=10))
detect(test_CIFAR10, Model_101_64x4d)
del Model_101_64x4d

"""## Both"""

train_CIFAR103 = torch.utils.data.DataLoader(dataset=datasets.CIFAR10('../data', train=True, download=True, transform=data_driven_transform_fn3),batch_size=256, shuffle=True, pin_memory=True, num_workers=2)

Model_50_32x4d = ResNext(model_variant='50_32x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data3_50_32x4d', benchmark=True)
trainer.fit(Model_50_32x4d, train_CIFAR103)
del trainer, Model_50_32x4d

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data3_50_32x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='50_32x4d',num_classes=10))
detect(test_CIFAR10, Model_50_32x4d)
del Model_50_32x4d

Model_101_32x8d = ResNext(model_variant='101_32x8d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data3_101_32x8d', benchmark=True)
trainer.fit(Model_101_32x8d, train_CIFAR103)
del trainer, Model_101_32x8d

Model_101_32x8d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data3_101_32x8d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_32x8d',num_classes=10))
detect(test_CIFAR10, Model_101_32x8d)
del Model_101_32x8d

Model_101_64x4d = ResNext(model_variant='101_64x4d',num_classes=10).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/data3_101_64x4d', benchmark=True)
trainer.fit(Model_101_64x4d, train_CIFAR103)
del trainer, Model_101_64x4d

Model_101_64x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/data3_101_64x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext(model_variant='101_64x4d',num_classes=10))
detect(test_CIFAR10, Model_101_64x4d)
del Model_101_64x4d

"""#CIFAR-10 with Multi-Tasking (3 types)

## Equal Weights
"""

Model_50_32x4d = ResNext_Model(model_variant='50_32x4d',num_classes=10,w1=0.5,w2=0.5).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/model_50_32x4d', benchmark=True)
trainer.fit(Model_50_32x4d, train_CIFAR10)
del trainer, Model_50_32x4d

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/model_50_32x4d/lightning_logs/version_9/checkpoints/epoch=99-step=19600.ckpt', ResNext_Model(model_variant='50_32x4d',num_classes=10,w1=0.5,w2=0.5))
detect(test_CIFAR10, Model_50_32x4d)
del Model_50_32x4d

"""## MSE more than Cross Entropy"""

Model_50_32x4d = ResNext_Model(model_variant='50_32x4d',num_classes=10,w1=0.3,w2=0.7).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/model2_50_32x4d', benchmark=True)
trainer.fit(Model_50_32x4d, train_CIFAR10)
del trainer, Model_50_32x4d

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/model2_50_32x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext_Model(model_variant='50_32x4d',num_classes=10,w1=0.3,w2=0.7))
detect(test_CIFAR10, Model_50_32x4d)
del Model_50_32x4d

"""## Cross Entropy more than MSE"""

Model_50_32x4d = ResNext_Model(model_variant='50_32x4d',num_classes=10,w1=0.7,w2=0.3).train().cuda()
trainer = pl.Trainer(accelerator='gpu', max_epochs=100, default_root_dir='/content/drive/MyDrive/DAI_Assignment_2/model3_50_32x4d', benchmark=True)
trainer.fit(Model_50_32x4d, train_CIFAR10)
del trainer, Model_50_32x4d

Model_50_32x4d = model_return('/content/drive/MyDrive/DAI_Assignment_2/model3_50_32x4d/lightning_logs/version_0/checkpoints/epoch=99-step=19600.ckpt', ResNext_Model(model_variant='50_32x4d',num_classes=10,w1=0.7,w2=0.3))
detect(test_CIFAR10, Model_50_32x4d)
del Model_50_32x4d