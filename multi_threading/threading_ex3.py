# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:19:50 2020

@author: matam
"""

import threading


def volume_cube(a):
    print("volume of cube",a*a*a)
    

def volume_square(a):
    print("volume of square",a*a)
    
    
t1=threading.Thread(target=volume_cube,args=(2,))
t2=threading.Thread(target=volume_square,args=(8,))

t1.start()
t2.start()