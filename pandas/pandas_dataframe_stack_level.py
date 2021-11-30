# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 07:34:27 2021

@author: matam
"""

import pandas as pd
import numpy as np


header = pd.MultiIndex.from_product([['Semester1','Semester2'],['Maths','Science']])
d=([[12,45,67,56],[78,89,45,67],[45,67,89,90],[67,44,56,55]])


df = pd.DataFrame(d,
                  index=['Alisa','Bobby','Cathrine','Jack'],
                  columns=header)
print(df)
# stack the dataframe


stacked_df=df.stack()
print(stacked_df)


stacked_df_lvl=df.stack(level=0)
print(stacked_df_lvl)