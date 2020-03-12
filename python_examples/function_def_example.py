# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:00:25 2020

@author: 666292
"""

str='hello'
def count_letter(content, letter):
    if (not isinstance(letter, str)) or len(letter) != 1:
      raise ValueError('`letter` must be a single character string.')
      
      
print(count_letter('hello','world'))      