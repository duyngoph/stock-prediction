import unittest
from src.models.arima import ARIMAModel
from src.models.sentiment import SentimentModel
from src.models.ensemble import EnsembleModel

class TestModels(unittest.TestCase):

    def setUp(self):
        self.arima_model = ARIMAModel()
        self.sentiment_model = SentimentModel()
        self.ensemble_model = EnsembleModel()

    def test_arima_model_fit(self):
        # Assuming we have a method to fit the model
        result = self.arima_model.fit(data='path_to_training_data')
        self.assertTrue(result)

    def test_sentiment_model_predict(self):
        # Assuming we have a method to predict sentiment
        prediction = self.sentiment_model.predict(text="The stock market is doing well.")
        self.assertIn(prediction, ['positive', 'negative', 'neutral'])

    def test_ensemble_model_predict(self):
        # Assuming we have a method to predict using the ensemble model
        prediction = self.ensemble_model.predict(data='path_to_data')
        self.assertIsInstance(prediction, float)  # Assuming the prediction is a float value

if __name__ == '__main__':
    unittest.main()