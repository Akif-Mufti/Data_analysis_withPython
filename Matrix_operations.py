# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:20:29 2016

@author: Aakif Mairaj Aka Akif Mufti

"""
import numpy as np

a= np.array([[1,2],[3,4]])
maga=np.sqrt(sum(a*a))
b= np.array([[4,-2],[-3,1]]) 
#calculatiing inverse
aInv= np.linalg.inv(a)

#dot with inverse

dinv= aInv.dot(a) #identity matrix
dinv2=a.dot(aInv) #idntity matrix
#matrix Determinant
detm= np.linalg.det(a)
#diagonal of a
diagn=np.diag(a)
#Other ways if i only want 1 2 3 4 in diagonals and rest 0
diage=np.diag([1,2,3,4,5])
#outer product c(i,j)=a(i)b(j)
v1= np.array([1,2])
v2= np.array([3,4])
op= np.outer(v1,v2)
#inner product 
ip=np.inner(v1,v2) #same as v1.dot(v2)

arr=np.array([[1,2,3],[3,4,5],[6,7,8]])
#calculating the sum of diagnol elements
sum_diag=np.diag(arr).sum()
# another funcion trace that calulates the sum of diagonal
sum_diag_2=np.trace(arr)

