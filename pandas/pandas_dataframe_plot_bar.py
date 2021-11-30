# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:57:42 2021

@author: matam
"""

import pandas as pd


height = [5, 17.5, 40, 48, 52, 69, 88]

years_to_fully_grow = [2, 8, 70, 1.5, 25, 12, 28]

index = ['lemon', 'cotton', 'neem',

         'hibscus', 'peepal', 'banyan', 'coconut']

df = pd.DataFrame({'height (in metres)': height, 
                   'Years taken to grow': years_to_fully_grow}, index=index)


print(df)

ax = df.plot.bar(rot=0)

axes = df.plot.bar(rot=0, subplots=True)