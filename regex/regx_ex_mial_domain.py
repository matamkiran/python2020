# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:52:01 2021

@author: Divya
"""
import re
result=re.findall('@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz,hello@gmail.com') 
print(set(result))
