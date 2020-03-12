# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:21:57 2020

@author: 666292
"""

import pickle

with open('date_time.pkl', 'rb') as p_f:
    data = pickle.load(p_f)
    print(data)