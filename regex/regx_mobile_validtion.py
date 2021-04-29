# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:56:33 2021

@author: Divya
"""

import re
li=['9000123456','8147375200','7890789456','1234']
for val in li:
 if re.match('[0-9]',val) and len(val)>9:
     pass
 else:
     print(val +" file doesn't match the naming standards !")
