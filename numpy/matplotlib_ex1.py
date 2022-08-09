import matplotlib.pyplot as plt 

year =[2019,2020,2021,2022]

population=[8.5 , 10.7 , 12.8 , 16.5]

plt.plot(year , population)

plt.title("Population year wise analysis")
plt.xlabel("years")
plt.ylabel("population in trillions")
plt.yticks([5,7,9,11,13,15])
#plt.show()