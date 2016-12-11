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
 69,
 69,
 71,
 76,
 71,
 73,
 73,
 74,
 74,
 69,
 70,
 73,
 75,
 78,
 79,
 76,
 74,
 76,
 72,
 71,
 75,
 77,
 74,
 73,
 74,
 78,
 73,
 75,
 73,
 75,
 75,
 74,
 69,
 71,
 74,
 73,
 73,
 76,
 74,
 74,
 70,
 72,
 77,
 74,
 70,
 73,
 75,
 76,
 76,
 78,
 74,
 74,
 76,
 77,
 81,
 78,
 75,
 77,
 75,
 76,
 74,
 72,
 72,
 75,
 73,
 73,
 73,
 70,
 70,
 70,
 76,
 68,
 71,
 72,
 75,
 75
]
# height is available as a regular list

# Import numpy
import numpy as np

# Create a Numpy array from height: np_height
np_height=np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m=np_height*0.0254

# Print np_height_m
print(np_height_m)
