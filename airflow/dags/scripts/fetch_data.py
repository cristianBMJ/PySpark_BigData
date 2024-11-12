import os
import yfinance as yf
from datetime import datetime, timedelta

today = datetime.now().date()
tomorrow = today + timedelta(days=1)

def fetch_data():
    # Ensure the data directory exists
    data_dir = "./data"
    os.makedirs(data_dir, exist_ok=True)  # Create directory if it doesn't exist

    try:
        data = yf.download("AAPL", start="2024-01-01", end=tomorrow)
        # Save to the new location
        data.to_csv(os.path.join(data_dir, "finance_data.csv"))
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_data()
