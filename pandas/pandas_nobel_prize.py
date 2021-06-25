# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 08:36:10 2021

@author: Divya
"""


# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import datetime as datetime

# Reading in the Nobel Prize data
nobel = pd.read_csv('C:/Users/Divya/complete.csv')

# Taking a look at the first several winners
print(nobel.head(n=6))


# Display the number of prizes won by the top 10 nationalities.
print(nobel['birth_country'].value_counts().head(10))

#Add a usa_born_winner column to nobel, where the value is True when birth_country is "United States of America".
nobel['usa_born_winner'] = nobel['birth_country'] == 'USA'

print(nobel)


# Calculating the proportion of USA born winners per decade
nobel['decade'] = (np.floor(nobel['awardYear'] / 10) * 10).astype(int)

print(nobel)

# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['gender'] == 'female'

print(nobel)

prop_female_winners = nobel.groupby(['decade','birth_country'], as_index=False)['female_winner'].mean()

print(prop_female_winners)


# Plotting female winners with % winners on the y-axis
from matplotlib.ticker import PercentFormatter
ax = sns.lineplot(x='decade', y='female_winner', hue='birth_country', data=prop_female_winners)
ax.yaxis.set_major_formatter(PercentFormatter(1.0))
