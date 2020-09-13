# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:50:50 2020

@author: 666292
"""

from collections import Counter

a=[1,1,10,2,3,1,2,4,6,6,3,5,7,8,9,8,9]

a=Counter(a)

print(a.most_common(5))