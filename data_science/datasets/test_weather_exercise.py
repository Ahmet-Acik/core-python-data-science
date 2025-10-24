import unittest
import pandas as pd

class TestWeatherExercise(unittest.TestCase):
    def test_load(self):
        weather = pd.read_csv('weather.csv')
        self.assertIn('temperature', weather.columns)
        self.assertEqual(weather.shape[0], 5)
    def test_date(self):
        weather = pd.read_csv('weather.csv')
        self.assertTrue(pd.to_datetime(weather['date'], errors='coerce').notnull().all())

if __name__ == '__main__':
    unittest.main()
