# src/indicators/get_indicator_data.py

from pathlib import Path

import pandas as pd
import questionary


def calculate_roc(df, length=13):
    """Calculate Rate of Change (ROC) for given DataFrame"""
    df["ROC"] = 100 * (df["Close"] - df["Close"].shift(length)) / df["Close"].shift(length)
    return df


def generate_signals(df):
    """Generate buy signals based on ROC threshold"""
    df["Signal"] = df["ROC"] < -15
    return df


def get_available_tickers(raw_data_dir):
    """Get sorted list of available tickers from raw data files"""
    data_files = list(raw_data_dir.glob("*_*_*_1d.csv"))
    tickers = sorted({f.name.split("_")[0] for f in data_files})
    return tickers


def process_stock_data(ticker, raw_data_dir, output_dir):
    """Process a single stock's data file"""
    try:
        # Find matching data file
        pattern = f"{ticker}_*_*_1d.csv"
        input_files = list(raw_data_dir.glob(pattern))

        if not input_files:
            raise FileNotFoundError(f"No data file found for {ticker}")

        if len(input_files) > 1:
            print(f"Multiple files found for {ticker}, using first match")

        input_file = input_files[0]
        output_file = output_dir / f"{ticker}_strategy.csv"

        # Read and process data
        df = pd.read_csv(input_file, parse_dates=["Date"])
        df = calculate_roc(df)
        df = generate_signals(df)

        # Save results
        df.to_csv(output_file, index=False)
        print(f"✅ Processed {ticker} ({len(df)} records)")
        print(f"📁 Output: {output_file}\n")

        return True

    except Exception as e:
        print(f"❌ Error processing {ticker}: {e!s}\n")
        return False


def main():
    """Main function to execute the strategy"""
    # Configure paths
    raw_data_dir = Path("data-files/raw")
    output_dir = Path("data-files/strategy-result")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get available tickers
    tickers = get_available_tickers(raw_data_dir)

    if not tickers:
        print("❌ No data files found in raw directory")
        print(f"Please add CSV files to {raw_data_dir.resolve()}")
        return

    # Select stocks using Questionary
    selected = questionary.checkbox(
        "Select stocks to analyze:",
        choices=tickers,
        instruction="(Space to select, ↑↓ to navigate, Enter to submit)",
        validate=lambda x: True if x else "Please select at least one stock",
    ).ask()

    if not selected:
        print("⛔ No stocks selected")
        return

    # Process selected stocks
    print("\n🚀 Processing stocks...\n")
    success_count = 0
    for ticker in selected:
        success = process_stock_data(ticker, raw_data_dir, output_dir)
        if success:
            success_count += 1

    # Show summary
    print(f"\n🎉 Successfully processed {success_count}/{len(selected)} stocks")
    print(f"Output directory: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
