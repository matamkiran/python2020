# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:54:02 2020

@author: 666292
"""

from scipy.misc import imread, imsave, imresize

img = imread('containers.jpg')
print(img.dtype, img.shape)