import os
import yfinance as yf
from datetime import datetime, timedelta

today = datetime.now().date()
tomorrow = today + timedelta(days=1)

def fetch_data():
    # Use the user's home directory
    home_dir = os.path.expanduser("~")
    data_dir = os.path.join(home_dir, "finance_data")
    
    # Create the directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    data = yf.download("AAPL", start="2020-01-01", end=tomorrow)
    
    # Save to the new location
    file_path = os.path.join(data_dir, "finance_data.csv")
    data.to_csv(file_path)

    print(f"Data saved to: {file_path}")
    print("Last 5 rows of fetched data:")
    print(data.tail())

if __name__ == "__main__":
    fetch_data()
