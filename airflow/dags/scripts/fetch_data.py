import yfinance as yf

def fetch_data():
    data = yf.download("AAPL", start="2020-01-01", end="2020-12-31")
    data.to_csv("./data/finance_data.csv")
