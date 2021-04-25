# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:42:04 2021

@author: Divya
"""
import random

try:
    def generator_otp():
        a=random.choice(range(1000,9999))
        yield a
        b=random.choice(range(1000,9999))
        yield b
        c=random.choice(range(1000,9999))
        yield c
    
    s=generator_otp()
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
except(StopIteration):
    print("maximum tries exceeded")
except(Exception):
    print("Unexpected error occurred please check your code")