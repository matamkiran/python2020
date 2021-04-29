# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:17:02 2021

@author: Divya
"""
import re 

substring="regex"

s1="""we are learning regex in python
      its very useful
    """
s2="""regexstring we are learning regex in python
      its very useful
    """

print(re.search(substring,s1, re.IGNORECASE))
print(re.search(substring,s2, re.IGNORECASE))

print(re.match(substring,s1, re.IGNORECASE))
print(re.match(substring,s2, re.IGNORECASE).group())

