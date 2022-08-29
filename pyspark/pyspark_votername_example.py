# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:45:24 2022

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


# Filter out voter_df where the VOTER_NAME contains an underscore
voter_df = voter_df.filter(~ F.col('VOTER_NAME').contains('a'))

print(voter_df.show())
