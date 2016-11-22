# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:03:03 2016

@author: Aakif Mairaj Aka Akif Mufti

"""
# problem Ax = b
# A^-1Ax =x=A^-1b
import numpy as np
a= np.array([[1,2],[3,4]])
b= np.array([3,4])

x= np.linalg.inv(a).dot(b)

#built in function called solve
x1=np.linalg.solve(a,b)


