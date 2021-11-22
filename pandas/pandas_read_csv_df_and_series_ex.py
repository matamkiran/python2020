# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 07:55:58 2021

@author: matam
"""

import pandas as pd
# Load the airquality dataset
airquality = pd.read_csv('air-quality.csv', index_col='Date')

print(airquality.head())

data=airquality.mean()

print(type(data))

print(data)

print(data['Ozone'])

df=pd.DataFrame(data)
print(df)


print(data.to_frame())
#print(type(df))

#airquality['mean']=data

#print(airquality['mean'])