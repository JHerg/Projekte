import unittest
from unittest.mock import patch
import test_forecast

class TestForecast(unittest.TestCase):
    @patch('test_forecast.random.uniform', return_value=0)
    def test_predict_visitors_temp_below_20_no_rain(self, mock_uniform):
        # 10°C, no rain -> 100 + 0 = 100
        result = test_forecast.predict_visitors(10, is_raining=False)
        self.assertEqual(result, 100)

    @patch('test_forecast.random.uniform', return_value=0)
    def test_predict_visitors_temp_above_20_no_rain(self, mock_uniform):
        # 25°C, no rain -> 100 + 5*20 = 200
        result = test_forecast.predict_visitors(25, is_raining=False)
        self.assertEqual(result, 200)

    @patch('test_forecast.random.uniform', return_value=0)
    def test_predict_visitors_temp_below_20_rain(self, mock_uniform):
        # 10°C, rain -> 100 * 0.5 = 50
        result = test_forecast.predict_visitors(10, is_raining=True)
        self.assertEqual(result, 50)

    @patch('test_forecast.random.uniform', return_value=0)
    def test_predict_visitors_temp_above_20_rain(self, mock_uniform):
        # 25°C, rain -> 200 * 0.5 = 100
        result = test_forecast.predict_visitors(25, is_raining=True)
        self.assertEqual(result, 100)

    @patch('test_forecast.random.uniform', return_value=5.5)
    def test_predict_visitors_with_randomness(self, mock_uniform):
        # 20°C, no rain -> 100. Plus 5.5 noise -> 105
        result = test_forecast.predict_visitors(20, is_raining=False)
        self.assertEqual(result, 105)

if __name__ == '__main__':
    unittest.main()
