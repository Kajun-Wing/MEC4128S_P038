# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:24:24 2022

@author: kajun
"""

import numpy as np
import pandas as pd
import cv2 as cv
import csv
import time
"""
NB:
ALWAYS CHECK 4 THINGS:
1) Correct PATH to write csv file
2) Correct place(WHERE) the images are coming from
3) Correct csv file NAME (to not overwrite others)
4) Correct IMAGE name you are trying to read
"""
total_frames = 250 #2125
data=501 #how wide the crop value is by 501x501
area = data * data

#path is where the csv file writes to
path= r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\CSV files\Normalised+Temp\Top_left\\'
# where is where the images are
where= r'C:\Users\kajun\Documents\0_UCT\2022\Sem 2 2022\MEC4128S\test\Normalised+Temp\Top_left\\'

# open the file in the write mode
f = open(path + "Ice-concentrations_TL_norm+temp_2.2.4.csv", "w", newline="")
# create the csv writer
writer = csv.writer(f)
header = ["Frame:", "Pancake pixels", "Frazil pixels","Total pixels", "%pancake","%frazil","Sea-ice concentration:" ]
# write a row to the csv file
writer.writerow(header)


#intializing the counting variables
x = 0
pancake = 0
frazil = 0

'''
New Data:
pancake ice range : -2.7 to -2.5
pancake corresponds to greyscale: 110 - 127

frazil ice range : -1.8 to -2.0
frazil corresponds to greyscale: 170 - 187
'''
#creating the grey scale value ranges to look into as zero value arrays
pancakes_min = 110
pancakes_max = 127
pancakes_range = pancakes_max - pancakes_min
frazil_min = 170
frazil_max = 187
frazil_range = frazil_max - frazil_min
pancake_gs_range = np.zeros(pancakes_range+1)
frazil_gs_range = np.zeros(frazil_range+1)
#populating the arrays with the correct values
for i in range(pancakes_range+1):
    pancake_gs_range[i]= pancakes_min + i
    
for i in range(frazil_range+1):
    frazil_gs_range[i]= frazil_min + i

# Log the start time
time_start = time.time()

#box commented out for testing purposes remove quotations to run code

while x<=total_frames-1:
    # Read in an image
    img = cv.imread(where+str(x+1001)+'_normal+temp.jpg',0)
    #finding the respective ice types with the gs range found previously
    for i in range(data):
        for j in range(data):
            if img[i,j] in pancake_gs_range:
                pancake +=1
                             
    for i in range(data):
        for j in range(data):
            if img[i,j] in frazil_gs_range:
                frazil +=1
 
   # calculating the % area basically the sea-ice concentration 
    per_pancake = pancake/area*100
    per_frazil = frazil/area*100   
    sea_ice_con = (pancake+frazil)/area*100         
    row = [x+1001, pancake, frazil,area, per_pancake, per_frazil, sea_ice_con]
    writer.writerow(row)         

    cv.waitKey(0)
    #setting the variables back to zero for the next frame
    pancake = 0
    frazil = 0
    #increases the count (moves to next frame)
    x = x+1  
    if x>total_frames-1:
        #Logging end time
        time_end = time.time()
        print("Finished")
        print ("It took %d seconds." % (time_end-time_start))
        break    

# close the file
f.close()




