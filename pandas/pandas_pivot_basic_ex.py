
import pandas as pd


data ={
       "category":
         ['mobile','tv','laptop','gadget','hardware'],
       'store':['filpkart','flipkart','amazon','CLIQ','alibaba'],
       'price':[10000,80000,100000,20000,5000]}


df=pd.DataFrame(data)

#print(df)


df_pivot=df.pivot(index='category',columns=['store'],values='price')

print(df_pivot)