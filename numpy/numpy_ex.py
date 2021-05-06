# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:55:57 2021

@author: Divya
"""

# Import `numpy` as `np`
import numpy as np

# Initialize `x` and `y`
x = np.ones((3,4))
y = np.random.random((5,1,4))

# Add `x` and `y`
print(x + y)

# Add `x` and `y`
np.add(x,y)

# Subtract `x` and `y`
np.subtract(x,y)

# Multiply `x` and `y`
np.multiply(x,y)

# Divide `x` and `y`
np.divide(x,y)

# Calculate the remainder of `x` and `y`
np.remainder(x,y)