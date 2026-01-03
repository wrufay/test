import pandas as pd
from pathlib import Path 

RAW_DATA_PATH = Path("data/raw/Waterloo Co-op Salaries List for Analysis.csv")
CLEAN_DATA_PATH = Path("data/processed/Waterloo Co-op Salaries List for Analysis.csv")

def load_raw_data():
    return pd.read_csv(RAW_DATA_PATH)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Drop duplicates
    df = df.drop_duplicates()

    # Remove rows without salary info
    df = df.dropna(subset=["salary"])

    # Convert salary to numeric (example)
    df["salary"] = (
        df["salary"]
        .astype(str)
        .str.replace(r"[^0-9.]", "", regex=True)
        .astype(float)
    )

    # Remove invalid salaries
    df = df[df["salary"] > 0]

    return df

def main():
    df_raw = load_raw_data()
    df_clean = clean_data(df_raw)

    CLEAN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)

    print(f"Cleaned data saved to {CLEAN_DATA_PATH}")

if __name__ == "__main__":
    main() 
