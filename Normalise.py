# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:47:41 2022

@author: kajun
"""
from collections import deque
import numpy as np
import cv2 as cv
import os
import time
'''
#Normalise finds the average of the top right and bot left corners "\n"
#and linearizes all the values along the perpendicular diagonal to that average value
'''
data = 500 #500
datas = data + 1

# found usings the Finding_average_gs_values_points.py
mean_top_cor_gs = 149 #149-TL, 175-M
mean_bot_cor_gs = 182 #182-TL, 206-M
mean_mid_gs = 170 #170-TL , 192-M

#finding the difference betwwen the average values and actual values
ave_on_diag_gs = ((mean_bot_cor_gs + mean_top_cor_gs)/2) # = 165.5
dif_btw_corners_ave_gs = ave_on_diag_gs-mean_bot_cor_gs # = +-16.5
dif_btw_mid_gs = mean_mid_gs - ave_on_diag_gs #4.5


#creating blank arrays/matrix
ave_gs = np.zeros((datas,datas))

bot_cor_to_ave = np.zeros(data)
top_cor_to_ave = np.zeros(data)

#appending the found temps to the start of the list
bot_cor_to_ave[0] = mean_bot_cor_gs
top_cor_to_ave[0] = mean_top_cor_gs

#creates the linear difference to the mean temp from each corner
for i in range(1,data):
    bot_cor_to_ave[i] = (bot_cor_to_ave[i-1]+ dif_btw_corners_ave_gs/data)
    top_cor_to_ave[i] = (top_cor_to_ave[i-1] - dif_btw_corners_ave_gs/data)

#need to append the final mean value for completeness
bot_cor_to_ave = np.append(bot_cor_to_ave,[ave_on_diag_gs])
top_cor_to_ave = np.append(top_cor_to_ave,[ave_on_diag_gs])
top_cor_to_ave = top_cor_to_ave[::-1] #reverses the array

#creates the average temp matrix
for i in range(datas):
    for j in range(datas):
        ave_gs[i,j] = ave_on_diag_gs
       
#creating the bottom half matrix            
list1 = deque()
for i in range(datas):   
    list1.append(bot_cor_to_ave+i*(dif_btw_corners_ave_gs/data))

bot_half = np.array(list1)
bot_half = np.flip(bot_half,0)  

for i in range(datas):
    for j in range(datas):
        if i<j and i!=data:
            bot_half[i,j] = 0
        if i==j:
            bot_half[i,j] = 0
            
#creates the top half matrix            
list2 = deque()
for i in range(datas):   
    list2.append(top_cor_to_ave-i*(dif_btw_corners_ave_gs/data))

top_half = np.array(list2)

for i in range(datas):
    for j in range(datas):
        if i>j:
            top_half[i,j] = 0
        if i==j:
            top_half[i,j] = 0

#adding them to make the linear matrix
linear = bot_half + top_half       
# create the normalized matrix by subtracting thr linearized matrix from ave_gs value matrix  
normalizer = ave_gs- linear
#adds the middle diagonal entries on the matrix
for i in range(datas):
    for j in range(datas):
        if i==j:
            normalizer[i,j] = -dif_btw_mid_gs

#normalizing the frames
total_frames = 2125 #2125
x = 0
# where to look for images in directory
where = r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Cropped frames\Cropped_frames_M//'
# where to put the images
path = r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Normalised\Middle\Normalised'

#box commented out for testing purposes need to remove the quotation marks to run code 
'''
# Log the start time
time_start = time.time()

while x<=total_frames-1:
# Read in an image
    img = cv.imread(where+str(x+1)+'_cropped.jpg',0)
    normal = img + normalizer
    #writes the images to path
    cv.imwrite(os.path.join(path , str(x+1)+'_normalised.jpg'), normal)
    cv.waitKey(0)
    x=x+1
    if x>total_frames-1:
        #Logging end time
        time_end = time.time()
        print("Finished")
        print ("It took %d seconds." % (time_end-time_start))
        break 
'''
