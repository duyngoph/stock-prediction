import unittest
from src.data.collect import collect_data
from src.data.preprocess import preprocess_data

class TestDataFunctions(unittest.TestCase):

    def test_collect_data(self):
        # Test if data collection function works correctly
        data = collect_data("^GSPC", "2015-01-01", "2025-01-01")
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_preprocess_data(self):
        # Test if data preprocessing function works correctly
        raw_data = collect_data("^GSPC", "2015-01-01", "2025-01-01")
        processed_data = preprocess_data(raw_data)
        self.assertIsNotNone(processed_data)
        self.assertGreater(len(processed_data), 0)
        self.assertIn('Date', processed_data.columns)

if __name__ == '__main__':
    unittest.main()