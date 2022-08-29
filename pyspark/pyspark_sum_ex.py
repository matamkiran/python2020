# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 23:35:50 2022

@author: matam
"""



# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
import pandas as pd
import numpy as np

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)

# Don't change this file path
file_path1 = "flights.csv"

# Read in the airports data
flights = my_spark.read.csv(file_path1, header=True)

# Show the data
flights.show()

# Average duration of Delta flights

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()
