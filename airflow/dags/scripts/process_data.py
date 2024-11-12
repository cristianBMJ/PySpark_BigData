import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def process_data():   
    spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()
    
    try:
        df = spark.read.csv("./data/finance_data.csv", header=True, inferSchema=True)

        # Process data: Example of grouping by date and summing the Volume
        agg_df = df.groupBy("Date").agg(F.sum("Volume").alias("Total_Volume"))
        
        # Save processed data to the processed folder with overwrite mode
        processed_dir = "./data/processed_data"
        os.makedirs(processed_dir, exist_ok=True)  # Create directory if it doesn't exist
        agg_df.write.mode("overwrite").csv(processed_dir, header=True)
    except Exception as e:
        print(f"Error processing data: {e}")

# Call the function
if __name__ == "__main__":
    process_data()
