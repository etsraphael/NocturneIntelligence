# src/indicators/__init__.py
from .djia_weakness import DJIAWeakness
from .us_presidential_cycles import USPresidentialCycles

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
}
