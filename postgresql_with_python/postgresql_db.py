# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 20:07:25 2022

@author: matam
"""

import psycopg2
import csv
# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
conn = psycopg2.connect(host="127.0.0.1", 
                        port = 5432,
                        database="test", 
                        user="postgres", 
                        password="root")

print(type(conn))
# Create a cursor object
cur = conn.cursor()

print(type(cur))

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("SELECT id,ename,sal FROM employees")
query_results = cur.fetchall()
print(query_results)
print(type(query_results))


row=['id','name','salary']
# reading csv file 
with open("emp_data.csv", 'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(row)
    writer.writerows(query_results)

records=open("emp_data.csv",'r')
print(records)
print(type(records))

for record in csv.reader(records):
    print(record)