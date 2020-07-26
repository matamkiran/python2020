# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:27:25 2020

@author: matam
"""

import time as t

print(t.ctime())


for count in range(5):
    print(t.ctime())
    t.sleep(2.5)