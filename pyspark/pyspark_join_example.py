# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 18:39:22 2022

@author: matam
"""


# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


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


# Don't change this file path
file_path = "planes.csv"

# Read in the airports data
planes = my_spark.read.csv(file_path, header=True)

# Show the data
planes.show()

# Average duration of Delta flights

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()


# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")

print(model_data)
"""
# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))

# Create the column plane_age
model_data = model_data.withColumn("plane_age", model_data.year - model_data.plane_year)

# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")

"""
print(model_data.show())


model_datas=model_data.groupBy(col("manufacturer"))


model_datas.count().show()