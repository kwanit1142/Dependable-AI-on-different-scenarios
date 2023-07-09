# -*- coding: utf-8 -*-
"""B19EE046_notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jIObJWRJMJhD4dYE9Fiva87qs_XH7vv1

##1. Mounting the Google Drive
##2. Cloning the Repository and pip-installing libraries.
##3. Reaching towards their working directory.
"""

from google.colab import drive
drive.mount('/content/gdrive')
!git clone https://github.com/kwanit1142/Intermediate-Level-Attack_DAI.git
!pip install pretrainedmodels
!pip install imageio

cd Intermediate-Level-Attack_DAI

"""##4. Reproducing and Visualizing on Pre-Existing CIFAR10 

##Note:- This section constitutes some shell commands which can be different to each other (like !wget, cd, %run), so run sequentially

###With Projection (Resnet18 being the Source Model)
"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks CW_Linf --num_batches=20 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""###With Projection (DenseNet121 being the Source Model)"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""###With Projection (GoogLeNet being the Source Model)"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""###With Projection (SENet18 being the Source Model)"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""###Without Projection (Resnet18 being the Source Model) 

*   in cifar10_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False

"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks CW_Linf --num_batches=20 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=20 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""###Without Projection (DenseNet121 being the Source Model) 

*   in cifar10_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False

"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=20 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""###Without Projection (GoogLeNet being the Source Model) 

*   in cifar10_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False

"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models GoogLeNet --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=20 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""###Without Projection (SENet18 being the Source Model) 

*   in cifar10_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False

"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks momentum_ifgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks fgsm --num_batches=50 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_cifar10.py --source_models SENet18 --transfer_models ResNet18 DenseNet121 GoogLeNet SENet18 --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=20 --batch_size=32
# %run '/content/Intermediate-Level-Attack_DAI/visualize_cifar10.ipynb'

!rm test.csv

"""##5. Trying the Approach, but this time on the selective Tiny-Imagenet 200 (Constitutes different distribution of samples, than that of Imagenet)

##Note:- This section constitutes some shell commands which can be different to each other (like !wget, cd, %run), so run sequentially

"""

from zipfile import ZipFile
import os
import numpy as np

!wget http://cs231n.stanford.edu/tiny-imagenet-200.zip

zip = ZipFile('/content/Intermediate-Level-Attack_DAI/tiny-imagenet-200.zip')
zip.extractall()
DATA_DIR = '/content/Intermediate-Level-Attack_DAI/tiny-imagenet-200' # Original images come in shapes of [3,64,64]
TRAIN_DIR = os.path.join(DATA_DIR, 'train') 
VALID_DIR = os.path.join(DATA_DIR, 'val')
val_img_dir = os.path.join(VALID_DIR, 'images')
fp = open(os.path.join(VALID_DIR, 'val_annotations.txt'), 'r')
data = fp.readlines()
val_img_dict = {}
for line in data:
    words = line.split('\t')
    val_img_dict[words[0]] = words[1]
fp.close()
for img, folder in val_img_dict.items():
    newpath = (os.path.join(val_img_dir, folder))
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if os.path.exists(os.path.join(val_img_dir, img)):
        os.rename(os.path.join(val_img_dir, img), os.path.join(newpath, img))

cd Intermediate-Level-Attack_DAI

"""###With Projection (Resnet18 being the Source Model)"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

"""###With Projection (DenseNet121 being the Source Model)"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

"""###With Projection (Alexnet being the Source Model)"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models alexnet --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models alexnet --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models alexnet --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

"""###With Projection (SqueezeNet1.0 being the Source Model)"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models SqueezeNet1.0 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models SqueezeNet1.0 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models SqueezeNet1.0 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

"""###Without Projection (Resnet18 being the Source Model)

*   in imagenet_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False
"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models ResNet18 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

"""###Without Projection (DenseNet121 being the Source Model)

*   in imagenet_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False
"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models DenseNet121 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

"""###Without Projection (AlexNet being the Source Model)

*   in imagenet_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False
"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models alexnet --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models alexnet --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models alexnet --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

"""###Without Projection (SqueezeNet1.0 being the Source Model)

*   in imagenet_config.py, turn use_projection=False
*   in attacks.py, switch ILA's function's with_projection=False
"""

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models SqueezeNet1.0 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models SqueezeNet1.0 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks momentum_ifgsm --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv

# Commented out IPython magic to ensure Python compatibility.
!python3 all_in_one_imagenet.py --source_models SqueezeNet1.0 --transfer_models ResNet18 DenseNet121 SqueezeNet1.0 alexnet --out_name=test.csv  --attacks Transferable_Adversarial_Perturbations --num_batches=40 --batch_size=4
# %run '/content/Intermediate-Level-Attack_DAI/visualize_imagenet.ipynb'

!rm test.csv