# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:40:54 2021

@author: Divya
"""
import re 

string1="my body temparature reading in recent days 95 96 97 93  "

str_pattern="\d{2}"

regex_pattern=re.compile(str_pattern)

print(regex_pattern)

lst=regex_pattern.findall(string1)

print(lst)
