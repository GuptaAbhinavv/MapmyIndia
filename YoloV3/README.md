### YOLOv3 (You only look once)

[YOLOv3](YOLOv3.pdf) is an updated version of the original [YOLO](YOLO.pdf).
Easy implementation of the pre-trained model can be  found on the [official website](https://pjreddie.com/darknet/yolo/). Also, easy steps to train it on selected datasets are given on the website. 

- [YOLO](YOLO.pdf) and [YOLOv3](YOLOv3.pdf) papers.

- I forked the original repository, darknet, having c++ implementation and all the necessary files for the implementation of pre-trained model - [GuptaAbhinavv/darknet](https://github.com/GuptaAbhinavv/darknet)

- Implementation of YOLOv3 using OpenCV in python based on [this](https://www.learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/).
Usage-
###### Getting weights-
  - `sudo chmod a+x getModels.sh`
  - `./getModels.sh`
##### Running code-
  - A single image
    - `python3 yolo_objD.py --image=bird.jpg`
  - A video file:
    - `python3 yolo_objD.py -- video=run.mpy`
