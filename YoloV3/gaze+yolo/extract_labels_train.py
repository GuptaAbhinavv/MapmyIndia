# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json


## List of all json files from where images have to be extracted
listfile = open("/home/intern/ods_job_120619/annotations/list.txt", "r")
jsonfiles=listfile.readlines()

filecount = 0
imgcount=0

for jsonfile in jsonfiles:
	filecount = filecount+1
	with open("/home/intern/ods_job_120619/annotations/"+jsonfile[:-1], "r") as read_file:
		data = json.load(read_file)
	dW = 1./1920
	dH = 1./1080

	## Adding all the classes in the list of classes (Currently - 3 classes)
	lis = []
	lis.append("signage")
	lis.append("traffic_sign")
	lis.append("traffic_light")

	## For maintaining list of training images
	imlist = open("/home/intern/newLabelsTrain/list.txt", "a")
	## For maintaining list of every train image with its corresponding url
	newlist = open("/home/intern/newLabelsTrain/newlist.txt", "a")

	## For maintaining list of test iamges
	imlist2 = open("/home/intern/newLabelsTest/list.txt", "a")
	## For maintaining list of every test image with its corresponding url
	newlist2 = open("/home/intern/newLabelsTest/newlist.txt", "a")

	for x in data:
		## Uncomment next line to filter hard negatives.
    	#if(len(data[x]["regions"]) < 1):continue
		filename = x.split('.')[0]

		## Splitting in the ratio 70:30
		if imgcount%100 < 70:
			fileobj = open("/home/intern/newLabelsTrain/" + filename + ".txt", "w")
			imgcount=imgcount+1
			imlist.write(filename + ".jpg"+ "\n")
			newlist.write(filename + ".jpg"+ "\n") 
			newlist.write("http://10.4.71.100/stage/maze/vs/trackSticker.php?action=getImage&image=" + filename + ".jpg" + "\n")
			for y in data[x]["regions"]:
				if(y["region_attributes"]["Label"]) not in lis: continue
				fileobj.write(str(lis.index(y["region_attributes"]["Label"])))
				#print(y["region_attributes"]["Label"])
				if(y["shape_attributes"]["name"] == u'rect'):
					xmin = y["shape_attributes"]["x"]
					ymin = y["shape_attributes"]["y"]
					xmax = xmin+y["shape_attributes"]["width"]
					ymax = ymin+y["shape_attributes"]["height"]
					X = (xmax+xmin)/2
					Y = (ymax+ymin)/2

					## YOLO training label format
					fileobj.write(" " + str(X*dW) +" ")
					fileobj.write(str(Y*dH)+" ")
					fileobj.write(str(y["shape_attributes"]["width"]*dW)+" ")
					fileobj.write(str(y["shape_attributes"]["height"]*dH))
					fileobj.write("\n")
				else:
					Xs = y["shape_attributes"]["all_points_x"]
					Ys = y["shape_attributes"]["all_points_y"]
					xmax = max(Xs)
					xmin = min(Xs)
					ymax = max(Ys)
					ymin = min(Ys)
					X = (xmax+xmin)/2
					Y = (ymax+ymin)/2
					width = xmax - xmin
					height = ymax - ymin

					## YOLO training label format
					fileobj.write(" " + str(X*dW) +" ")
					fileobj.write(str(Y*dH)+" ")
					fileobj.write(str(width*dW)+" ")
					fileobj.write(str(height*dH))
					fileobj.write("\n")
			fileobj.close()
		else:
			fileobj = open("/home/intern/newLabelsTest/" + filename + ".txt", "w")
			imgcount=imgcount+1
			imlist2.write(filename + ".jpg"+ "\n")
			newlist2.write(filename + ".jpg"+ "\n") 
			newlist2.write("http://10.4.71.100/stage/maze/vs/trackSticker.php?action=getImage&image=" + filename + ".jpg" + "\n")
			for y in data[x]["regions"]:
				if(y["region_attributes"]["Label"]) not in lis: continue
				fileobj.write(str(lis.index(y["region_attributes"]["Label"])))
				#print(y["region_attributes"]["Label"])
				if(y["shape_attributes"]["name"] == u'rect'):
					xmin = y["shape_attributes"]["x"]
					ymin = y["shape_attributes"]["y"]
					xmax = xmin+y["shape_attributes"]["width"]
					ymax = ymin+y["shape_attributes"]["height"]

					## Normal format for test files - class xmin xmax ymin ymax
					fileobj.write(" " + str(xmin) +" ")
					fileobj.write(str(xmax)+" ")
					fileobj.write(str(ymin)+" ")
					fileobj.write(str(ymax))
					fileobj.write("\n")
				else:
					Xs = y["shape_attributes"]["all_points_x"]
					Ys = y["shape_attributes"]["all_points_y"]
					xmax = max(Xs)
					xmin = min(Xs)
					ymax = max(Ys)
					ymin = min(Ys)
					fileobj.write(" " + str(xmin) +" ")
					fileobj.write(str(xmax)+" ")
					fileobj.write(str(ymin)+" ")
					fileobj.write(str(ymax))
					fileobj.write("\n")
			fileobj.close()
	print(filecount)
	imlist.close()
	newlist.close()
	imlist2.close()
	newlist2.close()
listfile.close()
print(imgcount)
