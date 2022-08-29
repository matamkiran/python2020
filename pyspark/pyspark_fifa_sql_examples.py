# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 01:36:55 2022

@author: matam
"""


# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

# Create my_spark
spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(spark)
# Don't change this file path
file_path = "Fifa2018_dataset.csv"

# Load the Dataframe 
fifa_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Check the schema of columns 
fifa_df.printSchema()

# Create a temporary view of fifa_df
fifa_df.createOrReplaceTempView('fifa_df_table')

# Construct the "query"
query = '''SELECT Potential,age  FROM fifa_df_table WHERE Nationality == "Germany"'''

# Apply the SQL "query"
fifa_df_germany_age = spark.sql(query)

# Generate basic statistics
fifa_df_germany_age.describe().show()

# Convert fifa_df to fifa_df_germany_age_pandas DataFrame
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()

# Plot the 'Age' density of Germany Players
fifa_df_germany_age_pandas.plot(kind='density')

plt.show()