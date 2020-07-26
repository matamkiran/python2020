# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:26:11 2020

@author: 666292
"""

import threading

def worker():
    print("worker")
    return
    
 

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()