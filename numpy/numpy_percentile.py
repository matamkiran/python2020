import numpy as np

#make this example reproducible
np.random.seed(0)

#create array of 100 random integers distributed between 0 and 500
data = np.random.randint(0, 500, 100)

#find the 37th percentile of the array
np.percentile(data, 37)

173.26

#Find the quartiles (25th, 50th, and 75th percentiles) of the array
a=np.percentile(data, [25, 50, 75])

print(a)
#print(array([116.5, 243.5, 371.5]))