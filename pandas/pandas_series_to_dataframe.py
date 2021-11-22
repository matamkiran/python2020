# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:05:42 2021

@author: matam
"""

import pandas as pd

item = ['Computer', 'Printer', 'Tablet', 'Desk', 'Chair']
series_item = pd.Series(item)

brand = ['A', 'B', 'C', 'D', 'E']
series_brand = pd.Series(brand)

price = [700, 150, 300, 450, 200]
series_price = pd.Series(price)

df_item= pd.DataFrame(series_item)
df_item = df_item.rename(columns = {0:'item'})

df_brand = pd.DataFrame(series_brand)
df_brand = df_brand.rename(columns = {0:'brand'})

df_price = pd.DataFrame(series_price)
df_price = df_price.rename(columns = {0:'price'})

df_all = pd.concat([df_item, df_brand, df_price ], axis=1)
print(df_all)
print(type(df_all))