## Intrinsic Calibration


###### BAG FILES(Preprocessing)
A bag is a file format in ROS for storing ROS message data. Bags -- so named because of their .bag extension -- have an important role in ROS, and a variety of tools have been written to allow you to store, process, analyze, and visualize them.
Bags are typically created by a tool like rosbag, which subscribe to one or more ROS topics, and store the serialized message data in a file as it is received. These bag files can also be played back in ROS to the same topics they were recorded from or even remapped to new topics.

We can use the following command to get the details of a bag file:
rosbag info foo.bag
The output might look something like this:

![Fig. 1](https://github.com/GuptaAbhinavv/MapmyIndia/blob/master/images/image1.png)

###### IMAGE EXTRACTION
The images contained in the bag file can be extracted using the below given code snippet:
Command to run the below code:
                 python program_name.py bag_file.bag path_name image_topic
bag_file: name of the bag file
path_name: path of the directory where images will be stored.
image_topic: topic of the image e.g. /frontNear/left/image_raw/


![Fig. 2: To extract the images out of a given bag file](images/image2.png)



Run the above code and store the corresponding images in the left and right directories(based on the topics of the messages).
Note that the directory for storing the left and right images needs to be created before running the code. 















###### FLOWCHART

![Fig. 3](images/image3.png)


###### IMPORTANT FUNCTIONS USED 
**_compare_ssim_**: Compute the mean structural similarity index between two images.

**_cv2.findChessboardCorners_**: Finds positions of the internal corners of the chessboard. Returns a boolean value depending on if the given shape of corners are found, also returns location of the corners if true.

**_cv2.cornerSubPix_**: The function iterates to find the sub-pixel accurate location of corners or radial saddle points.

**_cv2.drawChessboardCorners_**: Renders the detected chessboard corners.

**_cv2.calibrateCamera_**: Finds the camera intrinsic and extrinsic parameters from several views of a calibration pattern. Returns the rotation and translation matrix corresponding to each pattern. Also returns the camera intrinsic and distortion vector corresponding to lowest reprojection error.
**_cv2.projectPoints_**: Projects 3D points to an image. Used for calculating the reprojection error.
**_cv2.norm_**: Calculates the absolute or relative difference norm between the given image matrices. 

###### RESULTS
The algorithm takes 40 patterns from the given sample to calibrate the given camera. To cover all the possible orientations of the checkerboard, the selected sample images must be different in orientations. Three techniques have been used to select such samples-
Simply selecting first 40 images: Very low reprojection error suggests a possibility of images with similar orientations of the board been selected for calibration.  Therefore, a technique to select “good” images from the sample is required.

For right images:

![Fig. 4](images/image4.png)


For left images:

![Fig. 5](images/image6.png)


Skipping a few images after each image: Another approach we came up with is to skip about 20 to 25 images after selecting one so as to keep the variation amongst the selected images. The results obtained on including every 30th image are:
 ![Fig. 6](https://github.com/GuptaAbhinavv/MapmyIndia/blob/master/images/image6.png)
Calculating Structural Similarity index and filtering: Involves calculating the structural similarity index to compare every image with the previous image selected for calibration, based on the assumption that each image is more likely to be similar to the image previous to it as compared to others. A threshold value of SSIM is selected arbitrarily and the images with their value higher than the threshold are rejected. The results, obviously, are highly sensitive to the threshold value. 
######    a. Results with threshold SSIM = 0.65

![Fig. 7](images/image7.png)


######    b. Results with threshold SSIM = 0.62

![Fig. 8](images/image8.png)

A plot of threshold value of ssim of selected images(X) against the reprojection error(Y) - 
![plot](https://user-images.githubusercontent.com/29208697/62463900-dce69b00-b7a8-11e9-815c-d54797f7e13c.png)


