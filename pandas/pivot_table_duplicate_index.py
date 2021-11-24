# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 07:57:38 2021

@author: matam
"""


import pandas as pd


data ={
       "category":
         ['mobile','tv','laptop','gadget','hardware','hardware','tech','tech'],
       'store':['filpkart','flipkart','amazon','CLIQ','alibaba','alibaba','croma','croma'],
       'price':[10000,80000,100000,20000,5000,6000,9000,10000]}


df=pd.DataFrame(data)

print(df)

data_pivot=df.pivot_table(index="category",columns='store',aggfunc='mean',fill_value=0)

print(data_pivot)