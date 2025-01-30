import yfinance as yf

ticker = "AAPL"  # Change this to your preferred stock symbol
data = yf.download(ticker, start="2023-01-01", end="2024-01-01", interval="1d")

# Save data to CSV
csv_filename = f"data-files/{ticker}_data.csv"
data.to_csv(csv_filename)

print(f"Data saved to {csv_filename}")
