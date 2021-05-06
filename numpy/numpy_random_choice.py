# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 01:02:05 2021

@author: Divya
"""
import numpy as np
countries = ["Germany", "Switzerland", 
             "Austria", "Netherlands",
             "Belgium", "Poland", 
             "France", "Ireland"]
weights = np.array([83019200, 8555541, 8869537,
                    17338900, 11480534, 38413000, 
                    67022000, 4857000])
weights = weights / sum(weights)

for i in range(4):
    print(np.random.choice(countries,
                           p=weights, 
                           size=(3,),
                           replace=True))