# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:21:23 2016

@author: Aakif Mairaj aka Akif Mufti
"""
import numpy as np
#learning numpy 2D Arrays
# Create baseball, a list of lists
heights = [191,
 184,
 185,
 180,
 181,
 187,
 170,
 179,
 183,
 186,
 185,
 170
 ]
positions=['GK',
 'M',
 'A',
 'D',
 'M',
 'D',
 'M',
 'M',
 'M',
 'A',
 'M',
 'M',
 ]
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_heights=np.array(heights)
np_positions=np.array(positions)


# Heights of the goalkeepers: gk_heights
gk_heights= np_heights[np_positions=='GK']

# Heights of the other players: other_heights
other_heights=np_heights[np_positions!='GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
