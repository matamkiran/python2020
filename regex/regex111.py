# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:36:42 2021

@author: Divya
"""


import re
pattern=re.compile('AV')
result=pattern.findall('AV Analytics Vidhya AV')
print(result)
result2=pattern.findall('AV is largest analytics community of India')
print(result2)
