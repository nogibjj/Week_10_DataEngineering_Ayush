"""
Contains all the Functions required for PySpark Operations
"""

# Importing Libraries
from pyspark.sql import SparkSession


def create_spark(appName):
    """To Create Spark Session"""
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark


def end_spark(spark):
    """To Stop Spark Session"""
    spark.stop()
    return "Spark Session Stopped"


def query(spark, df, query, name):
    """Execute Spark SQL Query and return the result"""
    df = df.createOrReplaceTempView(name)

    return spark.sql(query).show()
