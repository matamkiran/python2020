# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 00:51:57 2021

@author: Divya
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("climate_austin.csv")

# Create a plot with color='red'
df.plot(color='red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()