# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 02:00:33 2021

@author: Divya
"""

# Import re module
import re
sentiment_analysis="@blueKnight39 check this https://www.tellyourstory.com for you @YourBestCompany!"
print(sentiment_analysis)
for tweet in sentiment_analysis:
  	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))
    

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))