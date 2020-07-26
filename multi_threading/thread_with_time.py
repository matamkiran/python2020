# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 11:50:55 2020

@author: matam
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:32:09 2020

@author: 666292
"""

import time
import threading

def thread1(i):
    time.sleep(3)
    print('No. printed by Thread 1: %d' %i)

def thread2(i):
    print('No. printed by Thread 2: %d' %i)
    
if __name__ == '__main__':
    
    t1 = threading.Thread(target=thread1, args=(10,))
    t2 = threading.Thread(target=thread2, args=(12,))
    # start the threads
    t1.start()
    t2.start()
    # join the main thread
    t1.join()
    t2.join()