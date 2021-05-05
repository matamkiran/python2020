# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:22:12 2021

@author: Divya
"""

import re 

text="please contact us support@team.com , callus@team.com my.hr001@team.com"

pattern= re.compile("@team",re.IGNORECASE)

result=pattern.search(text)

print(result.start())
print(result.end())
print(result.span())
print(result.group())
