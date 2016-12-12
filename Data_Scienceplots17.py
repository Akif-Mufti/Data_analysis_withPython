# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:19:27 2016

@author: Aakif Mairaj aka Akif Mufti
"""
#Following are the plots that represent V-I characteristics of a Flashlamp.
# One must Note that the V-I characteristics of a Flashlamp aren't similar to Traditional Flashlamp.
# Here K Represents the flashlamp Impedence Constant.
# V as the input voltage to the 200uF capacitor 
# Ip is the current peak

import numpy as np
import matplotlib.pyplot as plt

K=[17.2, 16.99, 15.87, 17.33, 16.59, 16.69, 17.39, 17.62, 16.86, 16.33, 17.77, 17.03, 17.08, 16.37, 17.05, 16.53, 17.12, 16.81, 16.61]
V=[500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000]
Ip= [180, 410, 680, 900, 1140, 1380, 1640, 1860, 2140, 2400, 2680, 2920, 3160, 3440, 3720, 3960, 4280, 4440, 4880]

col=['red',
 'green',
 'blue',
 'blue',
 'yellow',
 'black',
 'green',
 'red',
 'red',
 'green',
 'blue',
 'yellow',
 'green',
 'blue',
 'yellow',
 'green',
 'blue',
 'blue',
 'pink'
 ]
 #plot scatter
plt.scatter(x=V, y= Ip, s= np.array(K)*40, c= col, alpha=1)
plt.xlabel("Input Voltage (Volts)")
plt.ylabel("Flashlamp Peak-Current (Amps)")
plt.title("V-I characteristics of a Flashlamp")
plt.grid()
plt.show()

