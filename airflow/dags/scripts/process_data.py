import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from google.cloud import storage  # Import Google Cloud Storage client

def process_data():   
    spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()
    
    try:
        # Read data from local file
        df = spark.read.csv("./data/finance_data.csv", header=True, inferSchema=True)

        # Process data: Example of grouping by date and summing the Volume
        agg_df = df.groupBy("Date").agg(F.sum("Volume").alias("Total_Volume"))
        
        # Sort the DataFrame by Date
        agg_df = agg_df.orderBy("Date")
        
        # Save processed data to a single CSV file
        temp_path = "/tmp/agg_data_single.csv"
        agg_df.coalesce(1).write.mode("overwrite").option("header", "true").csv("/tmp/agg_data")

        # Find the actual CSV file inside the output directory
        for filename in os.listdir("/tmp/agg_data"):
            if filename.endswith(".csv"):
                csv_file = os.path.join("/tmp/agg_data", filename)
                break

        # Upload the CSV file to Google Cloud Storage
        bucket_name = "process_yfinance_demo"   # Replace with your GCS bucket name
        processed_file_path = "processed_data/agg_data.csv"  # Path in the bucket

        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(processed_file_path)
        blob.upload_from_filename(csv_file)

        # Clean up temporary files and directory
        os.remove(csv_file)
        os.rmdir("/tmp/agg_data")

    except Exception as e:
        print(f"Error processing data: {e}")

# Call the function
if __name__ == "__main__":
    process_data()
