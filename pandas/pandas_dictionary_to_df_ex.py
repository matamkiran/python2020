# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 07:35:27 2021

@author: matam
"""

import numpy as np
import pandas as pd


my_dict={1:[2,3],2:[4,5],3:[6,7]}

df=pd.DataFrame(my_dict,index=[10,20])

print(df)

df[4]=df.index
print(df)

#accessing via index of dataframe
print(df.loc[10])

print(df.iloc[1])
