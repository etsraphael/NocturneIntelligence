class DJIAWeakness:
    """Implementation of DJIA's Weakness indicator"""

    def __init__(self, roc_length=13, threshold=-15):
        self.name = "DJIA's Weakness"
        self.roc_length = roc_length
        self.threshold = threshold

    def calculate(self, df):
        """Calculate indicator values"""
        df = self._calculate_roc(df)
        df = self._generate_signals(df)
        return df

    def _calculate_roc(self, df):
        """Calculate Rate of Change (ROC)"""
        df["ROC"] = (
            100
            * (df["Close"] - df["Close"].shift(self.roc_length))
            / df["Close"].shift(self.roc_length)
        )
        return df

    def _generate_signals(self, df):
        """Generate buy signals based on ROC threshold"""
        df["Signal"] = df["ROC"] < self.threshold
        return df
