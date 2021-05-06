# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 00:57:11 2021

@author: Divya
"""


from numpy.random import choice
import numpy as np

professions = ["scientist", 
               "philosopher", 
               "engineer", 
               "priest", 
               "programmer"]

probabilities = [0.2, 0.05, 0.3, 0.15, 0.3]

print(choice(professions, p=probabilities))




