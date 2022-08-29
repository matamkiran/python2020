# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 19:25:36 2022

@author: matam
"""

# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

# Create my_spark
spark = SparkSession.builder.getOrCreate()

# Don't change this file path
file_path = "Fifa2018_dataset.csv"

# Load the Dataframe 
fifa_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Check the schema of columns 
fifa_df.printSchema()

# Create a temporary view of fifa_df
fifa_df.createOrReplaceTempView('fifa_df_table')

print(type(fifa_df))

query="select name ,age from  fifa_df_table"

df=spark.sql(query)

df.show(10)