# Sure, here's the contents for the file: /stock-prediction/stock-prediction/src/utils/helpers.py

def load_csv(file_path):
    import pandas as pd
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def save_csv(dataframe, file_path):
    """Save a DataFrame to a CSV file."""
    dataframe.to_csv(file_path, index=False)

def preprocess_text(text):
    """Basic text preprocessing for sentiment analysis."""
    import re
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower().strip()
    return text

def calculate_moving_average(data, window_size):
    """Calculate the moving average of a given data series."""
    return data.rolling(window=window_size).mean()