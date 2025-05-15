import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Clean and preprocess data (e.g., handle missing values)."""
    df.fillna(df.mean(), inplace=True)  # Fill missing values with column mean
    return df

