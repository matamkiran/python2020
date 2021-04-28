# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:20:34 2021

@author: Divya
"""

def parent(arg1,arg2):
    value=22
    mydict={'bangalore':'hebbal'}
    def child():
        print(value*2)
        print(mydict['bangalore'])
        print(arg1+arg2)
    return child

newfunc=parent(10,20)


#print(dir(newfunc))
print(newfunc.__closure__ is not None)
 
#for i in newfunc.__closure__:
    #print(i.cell_contents)
