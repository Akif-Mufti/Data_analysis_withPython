# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:10:49 2016

@author: Aakif Mairaj aka Akif Mufti
"""
#panda puts things in spread sheet like format
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
web_site = {'Day':[1,2,3,4,5,6,7],
            'Visitors':[12,13,24,56,67,89,5],'Bounce_Rate' :[34,56,78,89,90,54,56]}
#convert the dictionary into data frames
df= pd.DataFrame(web_site)
#to se the data frame you need to have A 
# generally when we make a Data Frame we represent it with df
#print(df)
#print(df.head())#Prints first five rows
#print(df.tail())#prints last five rows
#print(df.tail(2)) #prints last two
##when we have time series related data generally the index is going to be the day.
##in the following way we set the index to day
#print(df.set_index('Day')) #you are returned a new data frame 
##Now that we have set our index, one might thing of it to be permanent. If they see df.head(), it still starts with 0
#print(df.head())
#we can do it as under
df2 = df.set_index('Day')
print(df2.head())
#another way is
df.set_index('Day' ,inplace=True)
print(df.head())
#printing a particular column
print(df['Visitors'])
#another way of printing a particular column is making it like an attribue
print(df.Visitors) # No need to have those brackets as in Head()
print(df.Bounce_Rate) 
# how do you print double coloumn. It has a square bracket inside a square bracket
print(df[['Visitors','Bounce_Rate']])
# how can we convert the above into a list
print(df.Visitors.tolist())
# in pythor there are lists or Multi dimensional lists
# following stuff wont work out
#print(df[['Visitors','Bounce_Rate']].tolist())
#to make it HAPPEN WE HAVE TO GO TO TOP and TYPE "import numpy as np"
print(np.array(df[['Visitors','Bounce_Rate']])


