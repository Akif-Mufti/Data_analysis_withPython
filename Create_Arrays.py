# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:25:49 2016

@author: Aakif Mairaj aka Akif Mufti

"""
import numpy as np

#creating an array of all zeroes
Z=np.zeros(10) #Vector of 10 Zeros

#10x10 matrix of all Zeros

z2=np.zeros((10,10))
#10x10 matrix of all ones
z3=np.ones((10,10))
##10x10 matrix of all random numbers
z4=np.random.random((10,10))# this function gives us randomly distribute nos bw zeo and one
# Gausian distribution numbers need to passed seperately
G=np.random.randn(10,10)#Mean zero and variance one
# to calculate mean and variance
G.mean()
G.var()

