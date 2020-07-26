# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:24:58 2020

@author: 666292
"""

from _thread import start_new_thread
from time import sleep

threadId = 1 # thread counter
waiting = 2 # 2 sec. waiting time

def factorial(n):
    global threadId
    rc = 0
    
    if n < 1:   # base case
        print("{}: {}".format('\nThread', threadId ))
        threadId += 1
        rc = 1
    else:
        returnNumber = n * factorial( n - 1 )  # recursive call
        print("{} != {}".format(str(n), str(returnNumber)))
        rc = returnNumber
    
    return rc

start_new_thread(factorial, (5, ))
start_new_thread(factorial, (4, ))

print("Waiting for threads to return...")
sleep(waiting)