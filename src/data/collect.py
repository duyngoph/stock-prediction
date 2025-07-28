import yfinance as yf
import pandas as pd

def collect_sp500_data(start_date: str, end_date: str, filename: str) -> None:
    """
    Collect historical data for the S&P 500 index and save it to a CSV file.

    Parameters:
    - start_date: The start date for the data collection (format: 'YYYY-MM-DD').
    - end_date: The end date for the data collection (format: 'YYYY-MM-DD').
    - filename: The path to the CSV file where the data will be saved.
    """
    sp500 = yf.download("^GSPC", start=start_date, end=end_date)
    sp500.to_csv(filename)

def main():
    collect_sp500_data("2015-01-01", "2025-01-01", '../data/raw/sp500.csv')

if __name__ == "__main__":
    main()