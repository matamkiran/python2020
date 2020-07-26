# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 23:17:20 2020

@author: 666292
"""

import time
  
print("Current time is: " + time.ctime())
print(time.time())

print(time.time_ns())

print(time.localtime())

print(time.asctime())

print("Going to sleep for 3 seconds...")
time.sleep(3)
print("I am awake!")