import unittest
import pandas as pd

class TestWeatherExercise(unittest.TestCase):
    def test_load(self):
        weather = pd.read_csv('data_science/datasets/weather.csv')
        self.assertIn('temperature', weather.columns)
        self.assertEqual(weather.shape[0], 5)

    def test_date(self):
        weather = pd.read_csv('data_science/datasets/weather.csv')
        self.assertTrue(pd.to_datetime(weather['date'], errors='coerce').notnull().all())

    def test_humidity_and_wind_columns(self):
        weather = pd.read_csv('data_science/datasets/weather.csv')
        self.assertIn('humidity', weather.columns)
        self.assertIn('wind', weather.columns)

    def test_temperature_range(self):
        weather = pd.read_csv('data_science/datasets/weather.csv')
        self.assertTrue(weather['temperature'].between(10, 30).all())

 

if __name__ == '__main__':
    unittest.main()
