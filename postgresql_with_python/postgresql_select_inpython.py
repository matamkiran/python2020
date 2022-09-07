# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:57:30 2020

@author: 666292
"""

import psycopg2

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
conn = psycopg2.connect(host="127.0.0.1", 
                        port = 5432,
                        database="test", 
                        user="postgres", 
                        password="root")

print(conn)

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("SELECT * FROM employees")
query_results = cur.fetchall()
print(query_results)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()