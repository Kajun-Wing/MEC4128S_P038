# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:47:37 2022

@author: kajun
"""

import numpy as np
from decimal import *

# Formation ice tempertures, have a tolerance of +-0.1K
frazil = -2.47
pancake = -2.78

#creating arrays for using
data = 255 # number of data points
temps = np.zeros(data)
greyscale = np.zeros(256)

#temp scale
min_temp = -4
max_temp = -1
range_temp = max_temp - min_temp
#setting intial temperature in array
temps[0]=min_temp

#populating the arrays
for i in range(1,data):
  temps[i] = temps[i-1]+range_temp/255
  
for i in range(256):
    greyscale[i]= i
    
#fixing values for match    
temps = np.append(temps,[max_temp])  
temps = np.round(temps,5)

#Checking and visulizing data
#print(len(greyscale), len(temps))   
#print(greyscale, temps)

#function to find the respective temperature to greyscale value
def Greyvalues(w):
    actual_temp =  np.searchsorted(temps, Decimal(w))
    grey_value= greyscale[actual_temp]
    print(grey_value)


#function to find the respective greyscale to temperature value
def Temps(w):
    grey_value =  np.searchsorted(greyscale, Decimal(w))
    actual_temps= temps[grey_value]
    print(actual_temps)

#grey =  Greyvalues(0)
#ActTemps = Temps(round(149.2489))

'''
Old data:
pancake ice range : -2.867 to -2.689
pancake corresponds to greyscale: 96 - 112

frazil ice range : -2.556 to -2.378
frazil corresponds to greyscale: 122 - 138

New Data:
pancake ice range : -2.7 to -2.5
pancake corresponds to greyscale: 110 - 127

frazil ice range : -1.8 to -2.0
frazil corresponds to greyscale: 170 - 187
'''
