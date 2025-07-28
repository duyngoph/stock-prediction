from flask import Flask, request, jsonify
from src.models.arima import ARIMAModel
from src.models.sentiment import SentimentModel

app = Flask(__name__)

arima_model = ARIMAModel()
sentiment_model = SentimentModel()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    stock_name = data.get('stock_name')

    if not stock_name:
        return jsonify({'error': 'Stock name is required'}), 400

    # Get predictions from ARIMA model
    arima_prediction = arima_model.predict(stock_name)

    # Get sentiment analysis
    sentiment_prediction = sentiment_model.analyze(stock_name)

    # Combine predictions
    combined_prediction = {
        'arima_prediction': arima_prediction,
        'sentiment_prediction': sentiment_prediction
    }

    return jsonify(combined_prediction)

if __name__ == '__main__':
    app.run(debug=True)