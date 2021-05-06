# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:37:42 2021

@author: Divya
"""
# Import numpy
import numpy as np

height=[5.6,6.1,5.7,5.3,4.9,6.5,5.7]
weight=[70,60,75,77,65,50,55]
# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg=np.array(weight)*0.453592

# Calculate the BMI: bmi
bmi=np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)
