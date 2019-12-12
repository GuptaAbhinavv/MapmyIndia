# Training YOLO for Gaze Dataset


### Dataset Preparation
**Step1.** Prepare a list of json annotation files and create two new folders in 'trainLabels' and 'testLabels'.

**Step2.** Edit the paths in [extract_labels_train.py](extract_labels_train.py) according to your system and run the file. 

The folders 'trainLabels' and 'testLabels' now contain labels you need for training and testing.

**Step3.** The 'newlist.txt' file in each folder contains image name and corresponding urls. Run following commands to download training and testing images.

```
- mkdir trainImages
- cd trainImages
- xargs -n 2 curl -o < ../trainLabels/newlist.txt
- mkdir testImages
- cd testImages
- xargs -n 2 curl -o < ../testLabels/newlist.txt

```

### Training
**Step4.**

