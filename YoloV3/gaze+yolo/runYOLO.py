import os
import cv2
import subprocess

## List of testimages - Edit path accordingly.
listFile = "/aimldl-dat/data-gaze/AIML_Database_Test/newImagesTest/list.txt"

imagelist = open(listFile, "r");

images = imagelist.readlines();
i=0
for image in images:
	i=i+1
	## Terminal command needed for prediction. Edit path accordingly.
	command = "./darknet detector test /aimldl-dat/gaze+yolo4/gaze.data /aimldl-dat/gaze+yolo4/gaze-yolov3.cfg /aimldl-dat/gaze+yolo4/weights/gaze-yolov3.backup /aimldl-dat/data-gaze/AIML_Database_Test/newImagesTest/"+ image[:-1] + " -thresh 0.1"
	## label file corresponding to each image - Edit path accordingly.
	txtfile="/aimldl-dat/data-gaze/AIML_Database_Test/testPredictions2/"+image[:-5]+".txt"
	stdout = open(txtfile,"w")
	stderr = open("stderr.txt","wb")
	subprocess.call(command, stdout=stdout, stderr=stderr, shell=True)
	stdout.close()
	stderr.close()
## Uncomment next 3 lines to save prediction images in another folder. Edit path accordingly.	
#	prediction = cv2.imread("/aimldl-dat/darknet/predictions.jpg")
#	output = "/aimldl-cod/external/gaze+yolo2/YOLOoutPred/"+image[:-1]
#	cv2.imwrite(output, prediction)
	print(i)
	#print("\n")

