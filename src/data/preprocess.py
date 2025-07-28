import pandas as pd

def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the DataFrame by handling missing values and duplicates."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def transform_data(df):
    """Transform the DataFrame for analysis."""
    # Example transformation: Convert date column to datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    return df

def preprocess_data(file_path):
    """Main function to preprocess the data."""
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    processed_data = transform_data(cleaned_data)
    return processed_data