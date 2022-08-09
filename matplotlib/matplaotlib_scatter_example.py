# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:20:02 2022

@author: matam
"""

import matplotlib.pyplot as plt 
import numpy as np


wickets=np.arange(1,11)
score=[10, 100, 150 ,170 , 185, 200 , 215, 230 ,260 , 280]
print(wickets)

plt.title("Score Board")
plt.xlabel("Wickets ")
plt.ylabel("score")
plt.legend()
plt.scatter(wickets,score)


plt.plot( wickets,score,label="Runs Progress")

plt.show()