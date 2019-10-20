# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:35:47 2019

@author: Dashulik
"""

import cv2
import numpy as np 

# 0.creating a video object
video = cv2.VideoCapture(0) 
# 1. Variable
a = 0
# 2. While loop
while True:
    a = a + 1
    # 3.Create a frame object
    check, frame = video.read()
    # 4.show the frame!
    cv2.imshow("Smile!",frame)
    # 5.for playing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# 6. image saving
showPic = cv2.imwrite("webcam_picture.jpg",frame)
print(showPic)
# 8. shutdown the camera
video.release()
cv2.destroyAllWindows 

# 9. reading webcam picture from disc    
image = cv2.imread('webcam_picture.jpg')
# 10.  transform an image from BGR to Grayscale format by using cvtColor
grayscale_image_original = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 10.  transform an image from Grayscale to BGR format by using cvtColor
grayscale_image_final = cv2.cvtColor(grayscale_image_original, cv2.COLOR_GRAY2BGR)
# 11.  drawing red line
cv2.line(grayscale_image_final, (0,0), (640,480), (0, 0, 255), thickness=8, lineType=1)
# 12.  drawing blue polygon
cv2.rectangle(grayscale_image_final,(0,0),(146,228),(255,0,0),5) 
# 13. Comparing results
cv2.imshow('Before',image)
cv2.imshow('After', grayscale_image_final)
cv2.waitKey(0)
cv2.destroyAllWindows()