# Dependable AI on different scenarios

These Notebooks with their Question Statement and Reports, came under the course CSL7370, taken by Prof. Mayank Vatsa and Prof. Richa Singh.

## Lab-1 (Adversarial Attacks, DeepFake Detection and Audio Spoofing)

Question-1:

![images](https://github.com/kwanit1142/Dependable-AI-on-different-scenarios/assets/54277039/f46815c5-121f-445c-8c42-cb247f82a02a)

Using CIFAR10 dataset, implement FGSM on your own and use a basic CNN architecture with 3 convolution layers to show the impact of the attack. Use 2 deep-learning architecture and any 2 attacks out of which one has to be either Mask-based attack or PGD attack. 

Using the SVHN dataset, you need to show the impact of the attacks and compare and contrast them. 

Implement a deep learning architecture to detect adversarial attacks. The detection accuracy should be more than 70% of your attack (more the better).

Question-2:

![images](https://github.com/kwanit1142/Dependable-AI-on-different-scenarios/assets/54277039/a7d5f90f-2092-4165-9aac-fe578eb73ffe)

Create 100 deepfakes/faceswap from the existing tools of your choice using your own face images. Split this data into fine-tune and test sets (50-50). 

Finetune your model in Q1(iii) and test on the remaining 50 test samples and report the performance.

Question-3:

![_107790523_gettyimages-497254334](https://github.com/kwanit1142/Dependable-AI-on-different-scenarios/assets/54277039/e9197be9-5787-44d5-9f6f-e12b9950cc9d)

Record 1000 hindi and 1000 english sentences in your voice sampled from the given text files. Now, use any TTS system with an Indian speaker and generate audios using the text that you have recorded (Recorded audio will be considered as real and generated audio will be considered as fake). Please mention the TTS system that you have used.

Use an ASSIST architecture and train the architecture on the recorded and generated audios for spoof detection, i.e real v/s fake classification.

Use Pre-trained (trained on ASVSpoof2019LA) ASSIST and finetune it on your dataset for spoof classification.

Compare the performance for above 2 experiments using accuracy and EER metric.

Implement the Decision Error Trade-off (DET) curve from scratch and plot it for above two experiments.

Share the recorded and generated audios within separate folders respectively, using the drive link. Also, provide the sentences that you have used for recordings in an excel file. Combine all these folders and an excel file into one folder with a naming convention. Format of excel file content: Audio Number, Sentence.

## Lab-2 (Explainability and Bias)

Question-1:

Question-2:

![download](https://github.com/kwanit1142/Dependable-AI-on-different-scenarios/assets/54277039/4c545f32-71e4-452c-abd7-490875b3ecd7)

Select a recent paper on a SOTA performing model and reproduce the results on any one dataset mentioned in the paper. Do you observe any bias? Explain the type of bias you observed.

Try to mitigate the bias using the bias mitigation technique. In this, you have to select the paper related to bias mitigation and use it to mitigate the bias you found in part-B. Report the metrics values used in the paper. You are advised to select a cognitive bias mitigation paper to mitigate the cognitive bias in the computer vision task you select in part-A.

Try another approach of you rown to mitigate the bias using two techniques, either DATA method (Pre-Processing) or ALGORITHMIC method. Report the values of the same metric you used in part-C for these techniques also. 

Compare the bias mitigation techniques used in parts-C and D(a) and D(b) by taking in support of bias metrics. Report the changes you observed before and after applying bias mitigation techniques.

## Lab-3 (Federated Learning)

Question-1:

![Federated-Learning-vs-Fine-grained-Federated-Learning](https://github.com/kwanit1142/Dependable-AI-on-different-scenarios/assets/54277039/916989cb-5abf-4e95-a530-1e138df90e40)

Implement any federated learning algorithm of your choice using Pytorch with MNIST dataset on first client model, Coloured MNIST dataset on second client model, and SVHN dataset on third client model. Take 10k samples (i.e, 1k per class) for each dataset in training set on their respective client and 5k (i.e, 500 per class) samples of each dataset for test set.

a.) Perform (0-9) digit classification task using federated setup by performing aggregation at the central server.

b.) Report the class-wise accuracy results for all three dataset at their respective client side and at the central server also. Report overall classification Accuracy and Confusion Matrix.

c.) Write the mathematical explanation of the function used to perform the aggregation at the central server.

d.) Write the detailed explanation of the federated learning algorithm with the diagramatic representation used for the above solution.

e.) Compare the results of overall accuracy in federated setup with the baseline results calculated by combining all the datasets and trianing in non-federated setup. Do you observe any decrease/increase in accuracy for both the setups? State your answer with proper reasoning.

Question-2:
