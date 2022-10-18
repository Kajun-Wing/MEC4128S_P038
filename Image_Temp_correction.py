# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:20:19 2022

@author: kajun
"""

from collections import deque
import numpy as np
import cv2 as cv
import os
import time

data = 500 #500
datas = data + 1

gs_factor = 40.8 # for a change in 0.8 degrees in temp
#creating blank arrays/matrix
gs_factor_matrix = np.zeros((datas,datas))

#creates the normalize factor matrix
for i in range(datas):
    for j in range(datas):
         gs_factor_matrix[i,j] = gs_factor
         
#adjusing the gs in the frames
total_frames = 2125 #2125
x = 0
# where to look for images in directory
where = r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Normalised\Middle\Normalised//'
# where to put the images
path = r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Normalised+Temp\Middle'

#box commented out for testing purposes need to remove the quotation marks to run code 

# Log the start time
time_start = time.time()

while x<=total_frames-1:
# Read in an image
    img = cv.imread(where+str(x+1)+'_normalised.jpg',0)
    #cropping images to a square matrix at desired location
    gs_correct = img - gs_factor_matrix
    #writes the images to path
    cv.imwrite(os.path.join(path , str(x+1)+'_normal+temp.jpg'), gs_correct)
    cv.waitKey(0)
    x=x+1
    if x>total_frames-1:
        #Logging end time
        time_end = time.time()
        print("Finished")
        print ("It took %d seconds." % (time_end-time_start))
        break 
     