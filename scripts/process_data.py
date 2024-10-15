import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def process_data():
    spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()
    
    # Use the user's home directory
    home_dir = os.path.expanduser("~")
    data_dir = os.path.join(home_dir, "finance_data")
    
    # Load raw data from CSV
    raw_data_path = os.path.join(data_dir, "finance_data.csv")
    df = spark.read.csv(raw_data_path, header=True, inferSchema=True)
    
    # Process data: Example of grouping by date and summing the Volume
    agg_df = df.groupBy("Date").agg(F.sum("Volume").alias("Total_Volume"))
    
    # Save the aggregated data
    processed_data_path = os.path.join(data_dir, "processed_data.csv")
    agg_df.write.csv(processed_data_path, header=True, mode="overwrite")
    
    # Read the processed data
    processed_df = spark.read.csv(processed_data_path, header=True, inferSchema=True)
    
    # Show the last 5 rows
    print("Last 5 rows of processed data:")
    processed_df.orderBy(F.desc("Date")).show(5, truncate=False)

# Call the function
if __name__ == "__main__":
    process_data()
