# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 07:43:42 2021

@author: matam
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 07:23:52 2021

@author: matam
"""

import requests
import re

url = "https://api.stackexchange.com/2.3/tags?order=desc&sort=popular&site=stackoverflow"
res = requests.get(url)
text = res.json()
print(text)

data =dict(text)

print(data)

list_tags=data['items']

for value in list_tags:
        if(re.match("\D{6}",str(value['name']))):
            print(value['name'] + ": " + str(value['count']))
