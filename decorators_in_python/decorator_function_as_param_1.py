# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 07:40:33 2021

@author: matam
"""

import time 

def my_parent(func):
    def my_child():
        print("before function")
        print(time.time())
        print(time.sleep(5))
        func()
        print("after function")
        print(time.time())

    return my_child



@my_parent
def myownfunction():
    print("its my function in p-python")

@my_parent  
def yourfunction():
    print("its client function")
@my_parent   
def yourfunction2():
    print("its client function - 2")

@my_parent
def yourfunction3():
    print("its client function- 3")
    
def yourfunction4():
    print("its client function - 4")
    
    
    
myownfunction()
yourfunction()
yourfunction2()
yourfunction3()
yourfunction4()