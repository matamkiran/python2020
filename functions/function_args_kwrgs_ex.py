# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 08:03:06 2021

@author: Divya
"""

def myfunction(*args,**kwargs):
        print(args)
        print(kwargs)

myfunction('ajay','akbar','risma',firstname="ajay",secondname="kumar")