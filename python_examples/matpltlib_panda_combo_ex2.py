# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:44:30 2020

@author: 666292
"""

import matplotlib.pyplot as plt

import pandas as pd 

degrees=pd.read_csv('D:/python_docs/bachelor_degree_women_data.csv')

year=degrees['Year']
physical_sciences=degrees['Physical Sciences']
computer_science=degrees['Computer Science']

# Create plot axes for the first line plot
plt.axes([0.05,0.05,0.425,0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
plt.axes([0.525,0.05,0.425,0.9])


# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')


# Display the plot
plt.show()
