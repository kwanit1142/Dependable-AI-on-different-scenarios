# Dependable-AI-on-different-scenarios

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
