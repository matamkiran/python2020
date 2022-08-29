# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 23:55:12 2022

@author: matam
"""


# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)

# Don't change this file path
file_path1 = "flights.csv"



# Read in the airports data
flights = my_spark.read.csv(file_path1, header=True)


# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()

# Group by origin
by_origin = flights.groupBy("origin")


by_plane.count().show()