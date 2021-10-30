# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:08:05 2021

@author: 666292
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:57:30 2020

@author: 666292
"""

import psycopg2
import pandas as pd

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:


data = pd.read_excel("CR_DEPLOYMENT_REQUESTS_LOGGER_V2.xlsx")

df = pd.DataFrame(data[:15], columns= ['SR NO','RFC NO','Date and Day of Entry'])

print(df)
df.set_index("SR NO", drop=True, inplace=True)

dictionary = df.to_dict(orient="index")

print(dictionary)
 

conn = psycopg2.connect(host="localhost", port = 5432, database="mydb", user="devopstest", password="devopstest@434")

# Create a cursor object
cur = conn.cursor()
print(conn)

mainlist=[]

for key,value in dictionary.items():
    mylist=[]
    for k,v in value.items():
        print(v)
        mylist.append(v)
    mainlist.append(tuple(mylist))
        
        #cur.execute("insert into cr_deployments(rfc_no,date_day) values")
print(mainlist)

for value in mainlist:
    cur.execute("insert into cr_deployments(rfc_no,date_day) values"+str(value))
    
conn.commit()       
"""
# A sample query of all data from the "vendors" table in the "suppliers" database
query_results = cur.fetchall()
print(query_results))

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
"""
cur.close()
conn.close()
