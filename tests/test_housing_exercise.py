import unittest
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class TestHousingExercise(unittest.TestCase):
    def test_load(self):
        housing = pd.read_csv('data_science/datasets/housing.csv')
        self.assertIn('median_house_value', housing.columns)

    def test_model(self):
        housing = pd.read_csv('data_science/datasets/housing.csv')
        housing['income_per_lat'] = housing['median_income'] / housing['latitude']
        X = housing[['longitude', 'latitude', 'median_income', 'income_per_lat']]
        y = housing['median_house_value']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # ...existing code...
        model = LinearRegression()
        model.fit(X_train, y_train)
        r2 = model.score(X_test, y_test)
        self.assertFalse(pd.isna(r2), "R² score is NaN")
        self.assertGreaterEqual(r2, 0)

if __name__ == '__main__':
    unittest.main()
