import glob
import os

import pandas as pd
import questionary


def process_file(file_path, length=13):
    """
    Reads a CSV file, calculates the Rate of Change (ROC) for the 'close' column,
    and generates a 'Buy' signal when ROC is below -15%.

    Parameters:
        file_path (str): Path to the raw CSV file.
        length (int): Lookback period for the ROC calculation (default 13).

    Returns:
        pd.DataFrame: DataFrame with added 'roc' and 'signal' columns.
    """
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Standardize column names to lowercase for consistency
    df.columns = [col.lower() for col in df.columns]

    # Ensure the 'close' column is available
    if "close" not in df.columns:
        raise ValueError("The CSV file does not contain a 'close' column.")

    # Compute the Rate of Change (ROC)
    df["roc"] = 100 * (df["close"] - df["close"].shift(length)) / df["close"].shift(length)

    # Generate signals: flag a "Buy" when ROC is below -15%
    df["signal"] = df["roc"].apply(lambda x: "Buy" if x < -15 else "")

    return df


def main():
    # Directories for raw data and strategy results
    raw_dir = "data-files/raw"
    strategy_dir = "data-files/strategy-result"

    # Create the output folder if it doesn't exist
    if not os.path.exists(strategy_dir):
        os.makedirs(strategy_dir)

    # Find all CSV files in the raw data folder
    pattern = os.path.join(raw_dir, "*.csv")
    files = glob.glob(pattern)

    if not files:
        print(f"No CSV files found in {raw_dir}.")
        return

    # Extract unique tickers from the filenames (assumes ticker is before the first underscore)
    tickers = sorted({os.path.basename(f).split("_")[0] for f in files})

    # Use questionary to let the user select a ticker
    selected_ticker = questionary.select("Select a stock ticker:", choices=tickers).ask()
    if not selected_ticker:
        print("No ticker selected. Exiting.")
        return

    # Filter files corresponding to the selected ticker
    ticker_pattern = os.path.join(raw_dir, f"{selected_ticker}_*.csv")
    ticker_files = glob.glob(ticker_pattern)

    if not ticker_files:
        print(f"No files found for ticker {selected_ticker}.")
        return

    # If multiple files exist for the ticker, let the user choose one
    if len(ticker_files) > 1:
        file_choice = questionary.select(
            "Multiple files found. Select a file:", choices=ticker_files
        ).ask()
        if not file_choice:
            print("No file selected. Exiting.")
            return
        file_path = file_choice
    else:
        file_path = ticker_files[0]

    print(f"Processing file: {file_path}")

    try:
        df_result = process_file(file_path)
    except Exception as e:
        print(f"Error processing file: {e}")
        return

    # Construct an output filename based on the input file's name
    base_name = os.path.basename(file_path)
    output_file = os.path.join(strategy_dir, f"strategy_{base_name}")

    # Save the resulting DataFrame to a new CSV file
    df_result.to_csv(output_file, index=False)
    print(f"Strategy results saved to: {output_file}")


if __name__ == "__main__":
    main()
