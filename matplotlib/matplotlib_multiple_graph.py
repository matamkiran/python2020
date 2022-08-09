
import matplotlib.pyplot as plt 

runs =[19,20,15,22,10,9]

overs=[1,2,3,4,5,6]


plt.plot( overs,runs,label="kholi")


runs1 =[1,4,15,19,20,19]

overs1=[1,2,3,4,5,6]

plt.plot( overs1,runs1,label="Rohitsharma",color='red')

plt.title("Score board analysis")
plt.ylabel("Overs")
plt.xlabel("Runs per over")

plt.legend()
plt.show()