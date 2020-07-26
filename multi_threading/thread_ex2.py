# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:12:49 2020

@author: matam
"""

import threading 
import time

def thread_delay(thread_name,delay):
    count=0
    while count<3:
        time.sleep(delay)
        count=count+1
        print(thread_name,'----->',time.time())
        

t1=threading.Thread(target=thread_delay,args=('t1',1))
t2=threading.Thread(target=thread_delay,args=('t2',3))


t1.start()
t2.start()

t1.join()
t2.join()

