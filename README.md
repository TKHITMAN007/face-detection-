# face-detection-
face detection in a video using open cv
Detecting no. of faces in the video:

I have used opencv for face detection. For this I needed library files which can perform face detection.
 I used the cascade haarcascade_frontalface_default.xml and loaded it using CascadeClassifier() function.
Video path is given and loaded.
Now with a while loop , each frame of the video is accessed using read().
Each frame is changed to gray for better detection.
Using face_cascade() , multiple faces are detected in each frame.
With a for loop a rectangular bounding box is drawn over each face and text above the box indicating the face number.
