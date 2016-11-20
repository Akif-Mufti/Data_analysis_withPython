# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:31:25 2016

@author: Aakif Mairaj aka Akif Mufti
"""

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([11,22,33,44,55])

dot=0

for i,j in zip(a,b):
    dot+=i*j #accumulating the dot_product in the variable dot
print(dot)    
#following gives us the element wise multiplication
a*b
print(a*b) 
#to make it dot we sum up the elements of a*b to get the dot
dot2= np.sum(a*b)
print(dot2)
#another way of doing this
sum(a*b)
# but np comes with a dot product function
dot3=np.dot(a,b)
#other ways
dot4=a.dot(b)
dot5=b.dot(a)
#magnitude of a and b
maga=np.sqrt(sum(a*a))
magb=np.sqrt(sum(b*b))
#it can be calculated as
maga2 = np.linalg.norm(a)
#cosine of angle between a and b
cosine_angle= a.dot(b)/(maga*magb )
#calculating actual angle from np.arccos()
actual_angle=np.arccos(cosine_angle)


