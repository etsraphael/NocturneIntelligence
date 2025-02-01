#!/usr/bin/env python3
import glob
import os

import matplotlib.pyplot as plt
import pandas as pd
import questionary


def parse_filename(file_path):
    """
    Parse a filename of the format:
      STOCK_YYYY-MM-DD_YYYY-MM-DD_interval.csv
    Returns (stock, start_date, end_date, interval) if successful.
    """
    filename = os.path.basename(file_path)
    parts = filename.split("_")
    if len(parts) < 4:
        return None
    stock = parts[0]
    start_date = parts[1]
    end_date = parts[2]
    interval = parts[3].replace(".csv", "")
    return stock, start_date, end_date, interval


def list_available_stocks(stock_files):
    """Prints the available stocks and their associated file details."""
    print("Available stocks and their data:")
    for stock, files in stock_files.items():
        for file_info in files:
            file_path, start_date, end_date, interval = file_info
            print(
                f"Stock: {stock} | File: {os.path.basename(file_path)} | "
                f"Timeframe: {start_date} to {end_date} | Interval: {interval}"
            )


def process_stock(stock, file_info):
    """Handles prompting for date range, data filtering, and plotting for a given stock."""
    file_path, available_start, available_end, available_interval = file_info

    print(f"\nFor stock {stock}:")
    print(f"Available Timeframe: {available_start} to {available_end}")
    print(f"Available Interval: {available_interval}")

    # Ask if the user wants to filter by a custom date range.
    custom_range = (
        input("Do you want to filter by a custom date range? (y/n): ").lower().strip()
    )
    if custom_range == "y":
        custom_start = input("Enter start date (YYYY-MM-DD): ").strip()
        custom_end = input("Enter end date (YYYY-MM-DD): ").strip()
    else:
        custom_start = available_start
        custom_end = available_end

    # Read CSV data, parsing the 'Date' column.
    try:
        df = pd.read_csv(file_path, parse_dates=["Date"])
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return

    # Convert custom dates to datetime.
    try:
        custom_start_dt = pd.to_datetime(custom_start)
        custom_end_dt = pd.to_datetime(custom_end)
    except Exception:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Filter the DataFrame to the specified date range.
    df_filtered = df[(df["Date"] >= custom_start_dt) & (df["Date"] <= custom_end_dt)]
    if df_filtered.empty:
        print("No data available in the specified date range.")
        return

    # Plot the Close prices over time.
    plt.figure(figsize=(10, 5))
    plt.plot(df_filtered["Date"], df_filtered["Close"], marker="o", linestyle="-")
    plt.title(f"{stock} Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    csv_dir = "data-files/raw"
    csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))
    if not csv_files:
        print("No CSV files found in", csv_dir)
        return

    # Build a dictionary mapping each stock symbol to its file(s) and metadata.
    stock_files = {}
    for file in csv_files:
        info = parse_filename(file)
        if info:
            stock, start_date, end_date, interval = info
            stock_files.setdefault(stock, []).append((file, start_date, end_date, interval))

    # Optionally list all available stocks and details.
    list_available_stocks(stock_files)

    # Create a sorted list of available stocks.
    available_stocks = sorted(stock_files.keys())

    # Use questionary to let the user select stocks with arrow keys.
    selected_stocks = questionary.checkbox(
        "Select the stock(s) you want to graph:", choices=available_stocks
    ).ask()

    if not selected_stocks:
        print("No stocks selected. Exiting.")
        return

    for stock in selected_stocks:
        # For simplicity, we take the first file for the stock.
        process_stock(stock, stock_files[stock][0])


if __name__ == "__main__":
    main()
