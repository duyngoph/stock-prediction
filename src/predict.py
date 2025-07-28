import pickle
from src.arima_module import *
from src.sentiment_module import *
from src.feature_engineering import *

def run_pipeline(news_headlines):
    df = download_sp500_data()
    arima_model = train_arima(df)
    arima_signal = predict_next_movement(arima_model, df['Close'].iloc[-1])
    
    sentiment_score = analyze_sentiment(news_headlines)
    
    features = build_feature_row(arima_signal, sentiment_score)
    
    clf = pickle.load(open("models/final_classifier.pkl", "rb"))
    X = [[features["arima_pred"], features["sentiment_score"]]]
    prediction = clf.predict(X)[0]
    
    return prediction, features