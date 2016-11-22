# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:01:27 2016

@author: Aakif Mairaj aka Akif Mufti

"""
import numpy as np

#Matrix is 2-D array or list of lists
M=np.array([[1,2],[3,4]])
#First index is the row , Second Index is the column
list1=[[1,2],[3,4]]
#THis will give elements in the first list
list1[0]

#this will give element in first row first column
list1[0][0]

#We can do the same with array
M[0][0]

#another way of doing it
M[0,0]
#numpy has a representation for matrix also , as under.
M2=np.matrix([[1,2],[4,7]])
#official documentation prohbits u from making use of matrices
a=np.array(M2)
#transpose
a.T
M.T
#Matrix is a two dimensional numpy array and vector is one dimensional.
