from .djia_weakness import DJIAWeakness

INDICATORS = {
    "djia_weakness": {
        "name": "DJIA's Weakness",
        "class": DJIAWeakness,
        "description": "Buy when ROC(13) < -15%",
    }
}
