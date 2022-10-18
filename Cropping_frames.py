# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:56:07 2022

@author: kajun
"""

import cv2 as cv
import os
import time

#declaring the total amount of frames
total_frames = 2125 #2125
#intializing loop variable
x = 0
# where to look for images in directory
where = r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Frames//'
# where to put the images
path = r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Cropped_frames_M'

# Log the start time
time_start = time.time()

while x<=total_frames-1:
# Read in an image
    img = cv.imread(where+str(x+1)+'.jpg',0)
    #cropping images to a square matrix at desired location
    cropped = img[290:791, 366:867] #Height by with #0:1080 (top to bottom),0:1232 (left to right)
    #writes the images to path
    cv.imwrite(os.path.join(path , str(x+1)+'_cropped.jpg'), cropped)
    cv.waitKey(0)
    x=x+1
    if x>total_frames-1:
        #Logging end time
        time_end = time.time()
        print("Finished")
        print ("It took %d seconds." % (time_end-time_start))

#image size : 1080 x 1232         
#cropped = img[0:501, 731:1232] #cropping the top corner square
# cropped = img[290:791, 366:867] ##cropping the middle square