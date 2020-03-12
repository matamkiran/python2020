# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:48:11 2020

@author: 666292
"""

def function(argument):{
  switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
  return switcher.get(argument, "nothing")
}
        
print(function(0))