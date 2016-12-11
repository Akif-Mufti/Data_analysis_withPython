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
update=[[  1.2303559 , -11.16224898,   1.        ],
       [  1.02614252,  16.09732309,   1.        ],
       [  1.02614252,  16.09732309,   1.        ],
       [  1.02614252,  16.09732309,   1.        ]
       ]
# baseball is available as a regular list of lists
# update is available as 2D Numpy array



# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# np_baseball is available



# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))
