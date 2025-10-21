import unittest
import os
import pandas as pd
import numpy as np
from data_science import pandas_intro

class TestPandasIntro(unittest.TestCase):
    def tearDown(self):
        # Clean up any files created by export
        if os.path.exists('pandas_intro_export.csv'):
            os.remove('pandas_intro_export.csv')

    def test_series_basics(self):
        s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
        self.assertEqual(s['b'], 20)
        s2 = pd.Series([1, np.nan, 3])
        self.assertEqual(s2.isnull().sum(), 1)
        self.assertTrue(np.array_equal(np.array(s2.fillna(0).values), np.array([1, 0, 3])))

    def test_dataframe_basics(self):
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        self.assertListEqual(list(df.columns), ['A', 'B'])
        self.assertTrue((df.iloc[0] == pd.Series({'A': 1, 'B': 3})).all())
        df2 = pd.DataFrame({'A': [2, 1], 'B': [4, 3]})
        sorted_df = df2.sort_values('A')
        self.assertTrue(sorted_df.iloc[0]['A'] == 1)
        df3 = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': [1, 2, 3]})
        pivot = df3.pivot_table(index='A', values='B', aggfunc='sum')
        self.assertEqual(pivot.loc['foo', 'B'], 3)

    def test_selection_and_filtering(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        filtered = df[df['A'] > 1]
        self.assertTrue((filtered['A'] > 1).all())
        self.assertTrue(np.array_equal(np.array(df['B'].values), np.array([4, 5, 6])))
        df_left = pd.DataFrame({'key': ['a', 'b', 'c'], 'val1': [1, 2, 3]})
        df_right = pd.DataFrame({'key': ['a', 'b', 'd'], 'val2': [4, 5, 6]})
        merged = pd.merge(df_left, df_right, on='key', how='outer')
        self.assertEqual(merged.shape[0], 4)
        self.assertIn('val1', merged.columns)
        self.assertIn('val2', merged.columns)

    def test_aggregation_and_plot(self):
        df = pd.DataFrame({'group': ['x', 'x', 'y'], 'value': [1, 2, 3]})
        group_mean = df.groupby('group')['value'].mean()
        self.assertEqual(group_mean.loc['x'], 1.5)
        self.assertEqual(group_mean.loc['y'], 3)
        # Export
        df.to_csv('pandas_intro_export.csv', index=False)
        self.assertTrue(os.path.exists('pandas_intro_export.csv'))

if __name__ == "__main__":
    unittest.main()
