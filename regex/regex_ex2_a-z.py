# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:42:28 2021

@author: Divya
"""

import re
li=['file1.txt','FILE2.txt','file3.txt']
for val in li:
 if re.match('[a-z]',val):
     pass
 else:
     print(val +" file doesn't match the naming standards !")
