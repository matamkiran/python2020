# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:39:50 2021

@author: matam
"""
import pandas as pd

import pandas as pd

#create two DataFrames
df1 = pd.DataFrame({'player': ['A', 'B', 'C', 'D', 'E'],
                    'points':[12, 5, 13, 17, 27]})

df2 = pd.DataFrame({'player': ['F', 'G', 'H', 'I', 'J'],
                    'points':[24, 26, 27, 27, 12]})

#"stack" the two DataFrames together
df3 = pd.concat([df1,df2], ignore_index=True)

#view resulting DataFrame
print(df3)