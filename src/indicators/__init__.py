# src/indicators/__init__.py
from .djia_weakness import DJIAWeakness
from .us_presidential_cycles import USPresidentialCycles
from .weekly_average_buy import WeeklyAverageBuyIndicator  # New indicator added

INDICATORS = {
    "djia_weakness": {
        "name": "DJIA's Weakness",
        "class": DJIAWeakness,
        "description": "Buy when ROC(13) < -15%",
    },
    "presidential_cycles": {
        "name": "US Presidential Cycles",
        "class": USPresidentialCycles,
        "description": "Buy during Election, Post-Election, and Pre-Election years",
    },
    "weekly_average_buy": {
        "name": "Weekly Average Buy Indicator",
        "class": WeeklyAverageBuyIndicator,
        "description": (
            "Buy when the current close is below the historical weekly average by a "
            "set threshold or if it falls on the historically cheapest weekday (if threshold is None)"
        ),
    },
}
