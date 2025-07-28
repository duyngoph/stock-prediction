import unittest
from src.api.endpoints import get_prediction

class TestAPI(unittest.TestCase):

    def test_get_prediction_valid(self):
        response = get_prediction("AAPL")
        self.assertIn("prediction", response)
        self.assertIn("explanation", response)

    def test_get_prediction_invalid(self):
        response = get_prediction("INVALID")
        self.assertEqual(response, {"error": "Invalid stock name"})

if __name__ == '__main__':
    unittest.main()