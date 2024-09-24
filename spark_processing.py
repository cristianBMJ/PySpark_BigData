from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Big Data Processing") \
    .getOrCreate()

# Load dataset (assuming CSV for example)
df = spark.read.csv("data/large_dataset.csv", header=True, inferSchema=True)

# Perform transformations
filtered_df = df.filter(col("some_column") > 1000)

# Aggregation example
agg_df = filtered_df.groupBy("category").agg({"value_column": "sum"})

# Save results to local storage
agg_df.write.csv("data/processed_output.csv")

# Stop the Spark session
spark.stop()
