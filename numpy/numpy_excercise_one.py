# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:44:32 2021

@author: Divya

Define a structured array with two columns. 
The first column contains the product ID,
 which can be defined as an int32.
 The second column shall contain the price for the product.
 How can you print out the column with the product IDs,
 the first row and the price for the third article
 of this structured array?

"""

import numpy as np
mtype = [('productid',np.int32),('price',np.float64)]

data=np.array([(34567,678.88),(34568,672.78),(34569,670.87),(34570,700.89)],
              dtype=mtype)

print(data[1])
print(data['productid'])
print(data[2]["price"])
               
               
               
               
               
               
               
               
               
               
               