# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:14:13 2022

@author: matam
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:13:44 2022

@author: matam
"""


# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()


# Don't change this file path
file_path1 = "flights.csv"

# Read in the airports data
flights = my_spark.read.csv(file_path1, header=True)

# Show the data
flights.show()

# Don't change this file path
file_path = "planes.csv"

# Read in the airports data
planes = my_spark.read.csv(file_path, header=True)

# Show the data
planes.show()


# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")

model_datas=model_data.groupBy(col("manufacturer"))

model_datas.count().show()