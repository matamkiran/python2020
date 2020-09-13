# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:08:49 2020

@author: 666292
"""

from math import sqrt

nums = {int(sqrt(x)) for x in range(1000)}

print(nums)  # Prints "{0, 1, 2, 3, 4, 5}
