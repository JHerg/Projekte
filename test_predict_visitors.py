import unittest
from unittest.mock import patch
from test_forecast import predict_visitors

class TestPredictVisitors(unittest.TestCase):

    @patch('random.uniform')
    def test_predict_visitors_temp_le_20_no_rain(self, mock_uniform):
        mock_uniform.return_value = 0
        self.assertEqual(predict_visitors(15, False), 100)
        self.assertEqual(predict_visitors(20, False), 100)

    @patch('random.uniform')
    def test_predict_visitors_temp_gt_20_no_rain(self, mock_uniform):
        mock_uniform.return_value = 0
        self.assertEqual(predict_visitors(21, False), 120)
        self.assertEqual(predict_visitors(25, False), 200)

    @patch('random.uniform')
    def test_predict_visitors_temp_le_20_rain(self, mock_uniform):
        mock_uniform.return_value = 0
        self.assertEqual(predict_visitors(15, True), 50)
        self.assertEqual(predict_visitors(20, True), 50)

    @patch('random.uniform')
    def test_predict_visitors_temp_gt_20_rain(self, mock_uniform):
        mock_uniform.return_value = 0
        self.assertEqual(predict_visitors(21, True), 60)
        self.assertEqual(predict_visitors(25, True), 100)

    @patch('random.uniform')
    def test_predict_visitors_random_noise(self, mock_uniform):
        mock_uniform.return_value = 5.5
        self.assertEqual(predict_visitors(20, False), 105)

        mock_uniform.return_value = -3.2
        self.assertEqual(predict_visitors(20, False), 96)

if __name__ == '__main__':
    unittest.main()
