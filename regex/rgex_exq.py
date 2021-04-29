# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:18:20 2021

@author: Divya
"""

import re
result = re.match('Ana', 'Analytics Vidhya AV')
print(result.start())
print(result.end())

result=re.search('Vid','AV Analytics Vidhya AV')
print(result.group())


result=re.findall("AV","AV Analytics Vidhya AV")
print(result)


result=re.sub('India','the World','In India AV is largest Analytics community of India')
print(result)