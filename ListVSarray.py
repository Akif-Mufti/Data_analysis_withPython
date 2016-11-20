# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:57:19 2016

@author: CarpeDIEM
"""

import numpy as np
list = [1,2,3,4]
a = np.array([1,2,34])

for i in list:
    print(i)
    
for i in a:
    print(i)
    
list.append(5)    

#a.append(56) we cant append in numpy array

#list = list + [4,6] #plus sign with list does concatenation

#a= a + [3,4,5] #plus sign with numpy array does vector addition

2*list #two times araay
2*a # adition 
#we can't expect element wise multiplication in list
# list**2 
l2= []
for e in list:
    l2.append(e*e)
    
a**2    

np.sqrt(a) #elementwise square root
np.log(a) #elementwise log
np.exp(a) # elementwise exponential
# if we have to do them for list , it requires foorloop ;which is slow, but vectors are fast 
