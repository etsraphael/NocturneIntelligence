import pandas as pd


class WeeklyAverageBuyIndicator:
    """
    Weekly Average Buy Indicator

    This indicator compares today's close with the historical average for its weekday.

    Two modes are available:
      - Threshold Mode: When a threshold_pct is provided (e.g., -2), a buy signal is generated
        if today's close is more than 2% below the historical average for that weekday.
      - Best-Day Mode: When threshold_pct is None, the indicator computes the historical average
        for each weekday and signals a buy only if today falls on the weekday with the lowest average close.

    Note: This indicator is simplistic and assumes that historical weekday performance predicts future lows.
    Use it with caution in trending or highly volatile markets.
    """

    def __init__(self, threshold_pct=None):
        """
        Parameters:
          threshold_pct (float or None): The percentage difference threshold (negative value expected).
                                         If provided, a buy is signaled when:
                                           (Close - HistoricalAvg) / HistoricalAvg * 100 < threshold_pct
                                         If None, the indicator signals a buy only on the weekday that is
                                         historically the cheapest.
        """
        self.name = "Weekly Average Buy Indicator"
        self.threshold_pct = threshold_pct
        self.best_day = None  # Will be set if threshold_pct is None

    def calculate(self, df):
        """
        Calculate the indicator signals.

        Expects a DataFrame `df` with a datetime index and a 'Close' column.
        If the DataFrame index is not datetime but a 'Date' column exists,
        it converts that column to datetime and sets it as the index.

        After processing, a 'Date' column is added (copied from the index)
        and reordered to be the first column.

        Returns the DataFrame with additional columns:
          - 'Date': the date (placed as the first column)
          - 'Weekday': numerical weekday (Monday=0, ..., Sunday=6)
          - 'HistoricalAvg': the average Close for that weekday (computed on the full dataset)
          - 'PctDiff': percent difference between today's close and the historical average
          - 'Signal': True if a buy signal is generated, else False.
        """
        # Ensure the index is datetime. If not, try converting the 'Date' column.
        if not pd.api.types.is_datetime64_any_dtype(df.index):
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"])
                df = df.set_index("Date")
            else:
                raise ValueError(
                    "DataFrame index must be a datetime type or contain a 'Date' column to convert."
                )

        # Calculate the weekday averages and signals.
        df = self._calculate_weekday_average(df)
        df = self._generate_signals(df)

        # Add a 'Date' column from the index.
        df["Date"] = df.index

        # Reorder columns so that 'Date' is the first column.
        cols = list(df.columns)
        # Remove the 'Date' column from its current location
        cols.remove("Date")
        # Insert it at the beginning
        cols.insert(0, "Date")
        df = df[cols]

        return df

    def _calculate_weekday_average(self, df):
        # Create a column for weekday (0=Monday, 6=Sunday; trading data typically use 0-4).
        df["Weekday"] = df.index.dayofweek

        # Compute the historical average close for each weekday over the entire DataFrame.
        avg_by_day = df.groupby("Weekday")["Close"].mean()

        # Map the corresponding historical average to each row based on its weekday.
        df["HistoricalAvg"] = df["Weekday"].map(avg_by_day)

        # Compute the percentage difference between the current Close and its historical average.
        df["PctDiff"] = 100 * (df["Close"] - df["HistoricalAvg"]) / df["HistoricalAvg"]

        # Store the daily averages for potential further use.
        self.avg_by_day = avg_by_day

        return df

    def _generate_signals(self, df):
        if self.threshold_pct is not None:
            # In threshold mode: signal if today's price is below the historical average by more than the threshold.
            df["Signal"] = df["PctDiff"] < self.threshold_pct
        else:
            # In best-day mode: determine the weekday with the lowest historical average.
            best_day = self.avg_by_day.idxmin()  # e.g., 1 if Tuesday is cheapest.
            self.best_day = best_day
            # Signal a buy only if today is that weekday.
            df["Signal"] = df["Weekday"] == best_day
        return df
