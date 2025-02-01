import os
from datetime import datetime, timedelta

import yfinance as yf


def get_valid_date(prompt, default_date):
    while True:
        date_str = input(prompt)
        if not date_str:
            return default_date
        try:
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return parsed_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def get_valid_interval(prompt, default_interval):
    valid_intervals = [
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ]
    while True:
        interval = input(prompt).strip().lower()
        if not interval:
            return default_interval
        if interval in valid_intervals:
            return interval
        print(f"Invalid interval. Valid options are: {', '.join(valid_intervals)}")


# Get user inputs with validation
today = datetime.today().date()
default_start = today - timedelta(days=5 * 365)  # Approximate 5 years

# Ticker input
while True:
    ticker = input("Enter stock ticker symbol (e.g., AAPL): ").strip().upper()
    if ticker:
        break
    print("Ticker cannot be empty. Please try again.")

# Date inputs
start_date = get_valid_date(
    f"Enter start date [YYYY-MM-DD] (default: {default_start}): ", default_start
)

end_date = get_valid_date(f"Enter end date [YYYY-MM-DD] (default: {today}): ", today)

# Ensure end date is after start date
while end_date <= start_date:
    print("End date must be after start date.")
    end_date = get_valid_date(f"Enter end date [YYYY-MM-DD] (default: {today}): ", today)

# Interval input
interval = get_valid_interval("Enter interval [1m,1h,1d,etc.] (default: 1d): ", "1d")

# Download data
try:
    print(
        f"\nDownloading {ticker} data from {start_date} to {end_date} ({interval} interval)..."
    )
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date + timedelta(days=1),  # Include end date
        interval=interval,
    )

    if data.empty:
        print("No data found for the given parameters.")
    else:
        # Create directory if it doesn't exist
        os.makedirs("data-files", exist_ok=True)

        # Save to CSV
        csv_filename = f"data-files/{ticker}_{start_date}_{end_date}_{interval}.csv"
        data.to_csv(csv_filename)
        print(f"\nSuccessfully saved {len(data)} records to {csv_filename}")

except Exception as e:
    print(f"\nAn error occurred: {e!s}")
