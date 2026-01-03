import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/Waterloo Co-op Salaries List for Analysis.csv")
CLEAN_DATA_PATH = Path("data/processed/coop_salaries_clean.csv")

def load_raw_data():
    return pd.read_csv(RAW_DATA_PATH) 
