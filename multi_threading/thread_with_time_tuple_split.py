# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:15:35 2020

@author: matam
"""

import time

print(time.localtime())

print(time.localtime(time.time()))

rec=time.localtime(time.time())
print(time.strftime("%m",rec))
print(time.strftime("%Z",rec))
print(time.strftime("%c",rec))
print(time.strftime("%a",rec))
print(time.strftime("%A",rec))
print(time.strftime("%b",rec))
print(time.strftime("%B",rec))
print(time.strftime("%I %p",rec))