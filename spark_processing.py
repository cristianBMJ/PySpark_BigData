from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from datetime import datetime, timedelta

today = datetime.now().date()
tomorrow = today + timedelta(days=1)



# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Big Data Processing") \
    .getOrCreate()

import yfinance as yf

# Download stock market data for a specific company (e.g., Apple)
data = yf.download("META", start="2023-09-01", end=tomorrow)
data.to_csv('data/finance_stock_data_META.csv')

# Load dataset (assuming CSV for example)
df = spark.read.csv("data/finance_stock_data_META.csv", header=True, inferSchema=True)

print( df.columns, "\n")

df.orderBy(df['Date'].desc()).show(5)
# Perform transformations
filtered_df = df.filter(col("Volume") > 10)

# Aggregation example
agg_df = filtered_df.groupBy("Date").agg({"Volume": "sum"})

agg_df.orderBy(agg_df['Date'].desc()).show(5)

# Save results to local storage
agg_df.write.csv("data/processed_output_1.csv")
print(today)
# Stop the Spark session
spark.stop()
