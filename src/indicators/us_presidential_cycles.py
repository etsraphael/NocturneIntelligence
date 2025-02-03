# src/indicators/presidential_cycles.py
import pandas as pd


class USPresidentialCycles:
    """Implementation of US Presidential Cycles indicator"""

    def __init__(self):
        self.name = "US Presidential Cycles"

    def calculate(self, df):
        """Calculate indicator values"""
        df = self._generate_signals(df)
        return df

    def _generate_signals(self, df):
        """Generate signals based on presidential cycle phase"""
        # Convert to datetime and extract year
        df["Date"] = pd.to_datetime(df["Date"])
        years = df["Date"].dt.year

        # Calculate cycle position (0-3)
        cycle_position = years % 4

        # Green phases: Election (0), Post-Election (1), Pre-Election (3)
        df["Signal"] = (cycle_position == 0) | (cycle_position == 1) | (cycle_position == 3)
        return df
