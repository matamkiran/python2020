# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:05:19 2020

@author: matam
"""

import _thread
import time

def thread_delay(thread_name,delay):
    count=0
    while count<3:
        time.sleep(delay)
        count=count+1
        print(thread_name,'----->',time.time())
        

_thread.start_new_thread(thread_delay,('t1',3))
_thread.start_new_thread(thread_delay,('t2',5))

        

