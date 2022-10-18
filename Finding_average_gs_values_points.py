# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:59:42 2022

@author: kajun
"""

import cv2 as cv
import os
import numpy as np
import time

# Declaring num of frames
total_frames=2125

#intializing the counting loop variables
x=0

#creating blank arrays for values
mid_cor = np.zeros(total_frames)
bottom_cor = np.zeros(total_frames)
top_cor = np.zeros(total_frames)

# path to find the images
where = r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Cropped frames\Cropped_frames_M//'

# Log the start time
time_start = time.time()

# appending the blank arrays with the relevent values
while x<=total_frames-1:
# Read in an image
    img = cv.imread(where+str(x+1)+'_cropped.jpg',0)
    #finding the right values in all the images
    top_cor[x] = img[0,500]
    bottom_cor[x] = img[50,0]
    mid_cor[x] = img[250,250]
    x=x+1
    if x>total_frames-1:
        #Logging end time
        time_end = time.time()
        print("Finished")
        print ("It took %d seconds." % (time_end-time_start))
        break 

#finds the average value of each array and returns 4 sig figs
mean_top = np.round(np.mean(top_cor),4)
mean_bot = np.round(np.mean(bottom_cor),4)
mean_mid = np.round(np.mean(mid_cor),4)

print("Mean top corner gs value =",mean_top)
print("Mean bottom corner gs value =",mean_bot)
print("Mean middle gs value =",mean_mid)

'''
Found values:
    
Top corner crop:
Mean found top grey value:149.2489 =149
Which correspond to a top cor temp of: -2.0784

Mean found bot grey value:182.0315 = 182
Which correspond to a bot cor temp of: -1.4314

Mean found mid grey value:169.8014 = 170
Which correspond to a bot cor temp of: -1.6667


Middle crop:
Mean found top grey value:174.8122 = 175
Which correspond to a top cor temp of: -1.5686

Mean found bot grey value:206.1238 = 206
Which correspond to a bot cor temp of: -0.9608

Mean found mid grey value:191.5713 = 192
Which correspond to a bot cor temp of: -1.2353

'''