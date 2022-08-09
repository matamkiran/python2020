# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:43:07 2022

@author: matam
"""

import matplotlib.pyplot as plt 
import numpy as np


items=["loan","crud","medicine","gold","vehicle","others"]
percentage=["18","5","12","18","28","19"]
color=["r","y","b","g","m","c"]


plt.title("GST")
plt.pie(percentage,labels=items,colors=color,startangle=90,radius=1.1,autopct="%1.2f%%")
plt.legend()
plt.show()
