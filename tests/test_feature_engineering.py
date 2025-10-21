import unittest
import pandas as pd
import numpy as np
from data_science import feature_engineering

class TestFeatureEngineering(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'height': [170, 180, 160],
            'weight': [70, 80, 60],
            'gender': ['M', 'F', 'F'],
            'date': ['2020-01-01', '2021-06-15', '2019-12-31']
        })

    def test_create_features(self):
        import math
        result = feature_engineering.create_features(self.df)
        self.assertIn('bmi', result)
        self.assertIn('year', result)
        self.assertTrue(math.isclose(float(result.loc[0, 'bmi']), 24.22, abs_tol=0.1))
        self.assertEqual(result.loc[0, 'year'], 2020)

    def test_log_transform(self):
        result = feature_engineering.log_transform(self.df, 'weight')
        self.assertIn('weight_log', result)
        self.assertTrue(np.allclose(result['weight_log'], np.log1p(self.df['weight'])))

    def test_scale_features(self):
        result = feature_engineering.scale_features(self.df, ['height', 'weight'])
        self.assertTrue(np.allclose(result['height'].mean(), 0, atol=1e-7))
        self.assertTrue(np.allclose(result['weight'].mean(), 0, atol=1e-7))

    def test_one_hot_encode(self):
        result = feature_engineering.one_hot_encode(self.df, ['gender'])
        self.assertIn('gender_M', result)
        self.assertIn('gender_F', result)
        self.assertEqual(result['gender_M'].sum(), 1)
        self.assertEqual(result['gender_F'].sum(), 2)

    def test_label_encode(self):
        result = feature_engineering.label_encode(self.df, 'gender')
        self.assertIn('gender_le', result)
        self.assertEqual(set(result['gender_le']), {0, 1})

    def test_bin_numerical(self):
        result = feature_engineering.bin_numerical(self.df, 'height', bins=3)
        self.assertIn('height_bin', result)
        self.assertTrue(result['height_bin'].notnull().all())

    def test_add_interactions(self):
        result = feature_engineering.add_interactions(self.df, ['height', 'weight'])
        self.assertTrue(any('height' in col and 'weight' in col for col in result.columns))
        self.assertTrue(any('height^2' in col or 'weight^2' in col for col in result.columns))

    def test_column_selector(self):
        selector = feature_engineering.ColumnSelector(['height', 'weight'])
        selected = selector.transform(self.df)
        self.assertListEqual(list(selected.columns), ['height', 'weight'])

    def test_example_pipeline(self):
        # Just check that it runs and produces correct shape
        df = pd.DataFrame({
            'height': [170, 180, 160],
            'weight': [70, 80, 60],
            'gender': ['M', 'F', 'F']
        })
        pipe = feature_engineering.Pipeline([
            ('select', feature_engineering.ColumnSelector(['height', 'weight'])),
            ('scale', feature_engineering.StandardScaler()),
            ('poly', feature_engineering.PolynomialFeatures(degree=2))
        ])
        features = pipe.fit_transform(df)
        self.assertEqual(features.shape[1], 6)  # 2 features + interactions + squares

if __name__ == "__main__":
    unittest.main()
