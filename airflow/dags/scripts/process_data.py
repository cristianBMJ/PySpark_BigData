from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def process_data():
    spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()
    
    # Load raw data from CSV
    df = spark.read.csv("./data/finance_data.csv", header=True, inferSchema=True)
    
    # Process data: Example of grouping by date and summing the Volume
    agg_df = df.groupBy("Date").agg(F.sum("Volume").alias("Total_Volume"))
    
    # Save processed data to the processed folder
    agg_df.write.csv("./data/processed_data.csv", header=True)
