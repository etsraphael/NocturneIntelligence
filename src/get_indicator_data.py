# src/indicators/get_indicator_data.py
from pathlib import Path

import pandas as pd
import questionary
from indicators import INDICATORS


def get_available_tickers(raw_data_dir):
    """Get sorted list of available tickers from raw data files"""
    data_files = list(raw_data_dir.glob("*_*_*_1d.csv"))
    tickers = sorted({f.name.split("_")[0] for f in data_files})
    return tickers


def process_stock_data(ticker, indicator, raw_data_dir, output_dir):
    """Process a single stock's data file"""
    try:
        # Find matching data file
        pattern = f"{ticker}_*_*_1d.csv"
        input_files = list(raw_data_dir.glob(pattern))

        if not input_files:
            raise FileNotFoundError(f"No data file found for {ticker}")

        input_file = input_files[0]
        output_file = output_dir / f"{input_file.stem}_{indicator['key']}_indicator.csv"

        # Read data and apply indicator
        df = pd.read_csv(input_file, parse_dates=["Date"])
        strategy = indicator["class"]()
        df = strategy.calculate(df)

        # Save results
        df.to_csv(output_file, index=False)
        print(f"✅ Processed {ticker} with {indicator['name']} ({len(df)} records)")
        print(f"📁 Output: {output_file}\n")
        return True

    except Exception as e:
        print(f"❌ Error processing {ticker}: {e!s}\n")
        return False


def main():
    """Main function to execute the strategy"""
    # Configure paths
    raw_data_dir = Path("data-files/raw")
    output_dir = Path("data-files/indicator-result")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get available tickers
    tickers = get_available_tickers(raw_data_dir)

    if not tickers:
        print("❌ No data files found in raw directory")
        print(f"Please add CSV files to {raw_data_dir.resolve()}")
        return

    # Create indicator choices
    indicator_choices = [{"name": f"{v['name']}", "value": k} for k, v in INDICATORS.items()]

    # Select indicator
    selected_indicator_key = questionary.select(
        "Select an indicator to use:",
        choices=indicator_choices,
        instruction="(↑↓ to navigate, Enter to select)",
    ).ask()

    if not selected_indicator_key:
        print("⛔ No indicator selected")
        return

    selected_indicator = {"key": selected_indicator_key, **INDICATORS[selected_indicator_key]}

    # Select stocks
    selected_tickers = questionary.checkbox(
        "Select stocks to analyze:",
        choices=tickers,
        instruction="(Space to select, ↑↓ to navigate, Enter to submit)",
        validate=lambda x: True if x else "Please select at least one stock",
    ).ask()

    if not selected_tickers:
        print("⛔ No stocks selected")
        return

    # Process selected stocks
    print("\n🚀 Processing stocks...\n")
    success_count = 0

    for ticker in selected_tickers:
        success = process_stock_data(ticker, selected_indicator, raw_data_dir, output_dir)
        if success:
            success_count += 1

    # Show summary
    print(f"\n🎉 Successfully processed {success_count}/{len(selected_tickers)} stocks")
    print(f"Indicator used: {selected_indicator['name']}")
    print(f"Output directory: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
