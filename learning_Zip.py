# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:23:44 2016

@author: Aakif Mairaj aka Akif Mufti
"""
 
l = [1,2,3,4]
m = [4,5,6,7]

#zip() will convert it into something like this [(1,4)(2,5)(3,6)(4,7)]


zipy = zip(l,m)



for x,y in zipy:
    print(x*y)
    
print(zipy)
#following sums all the elements of l
print(np.sum(l))