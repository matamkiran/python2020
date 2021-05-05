# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:10:39 2021

@author: Divya
"""

import re 

text="please contact us support@team.com , callus@team.com my.hr001@team.com"


result=re.finditer("[\w\.-]+@[\w\.-]+", text)

for res in result:
    print(res.group())
