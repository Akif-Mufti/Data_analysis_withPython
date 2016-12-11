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

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[2])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[2:4])
