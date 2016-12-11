# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:21:23 2016

@author: Aakif Mairaj aka Akif Mufti
"""
#learning numpy
height=[74,
 74,
 72,
 72,
 73,
 
 
]

weight=[180,
 215,
 210,
 210,
 188
 ]
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight)*0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)
