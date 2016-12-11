# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:21:23 2016

@author: Aakif Mairaj aka Akif Mufti
"""
import numpy as np
#learning numpy 2D Arrays
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy


# Create a 2D Numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape) 