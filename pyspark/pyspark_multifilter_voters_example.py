# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 00:34:20 2022

@author: matam
"""

# Import the pyspark.sql.types library
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

my_spark = SparkSession.builder.getOrCreate()


# Don't change this file path
file_path1 = "DallasCouncilVoters.csv"

# Read in the airports data
voter_df = my_spark.read.csv(file_path1, header=True)


# Show the distinct VOTER_NAME entries
voter_df.select(voter_df['VOTER_NAME']).distinct().show(40, truncate=False)

# Filter voter_df where the VOTER_NAME is 1-20 characters in length
voter_df = voter_df.filter('length(VOTER_NAME) > 0 and length(VOTER_NAME) < 20')

# Filter out voter_df where the VOTER_NAME contains an underscore
voter_df = voter_df.filter(~ F.col('VOTER_NAME').contains('.'))

print(voter_df)

# Show the distinct VOTER_NAME entries again
voter_df.select('VOTER_NAME').distinct().show(40, truncate=False)