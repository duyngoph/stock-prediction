import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def download_sp500_data(start="2015-01-01", end="2025-01-01"):
    df = yf.download("^GSPC", start=start, end=end)
    return df

def train_arima(df, order=(5,1,0)):
    model = ARIMA(df['Close'], order=order)
    model_fit = model.fit()
    return model_fit

def predict_next_movement(model_fit, last_price):
    forecast = model_fit.forecast(steps=1)
    return 1 if forecast[0] > last_price else 0