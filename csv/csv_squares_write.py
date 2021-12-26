import csv

nums=[[value,value**2] for value in range(1000) if(value%2==0)]


row=['number','square']
# reading csv file 
with open("sqaures_write", 'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    print(nums)
    writer.writerow(row)
    writer.writerows(nums)
    

