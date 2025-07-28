def build_feature_row(arima_pred, sentiment_score):
    return {
        "arima_pred": arima_pred,
        "sentiment_score": sentiment_score
    }