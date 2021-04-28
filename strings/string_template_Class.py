# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:43:14 2021

@author: Divya
"""

from string import Template 

subs = dict(who ="you" ,whom ="me")

file=Template("$who  owe the money to $whom").substitute(subs)

print(file)
