import unittest
import pandas as pd
import numpy as np
from data_science import data_cleaning

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        # Add a true duplicate row for testing
        self.df = pd.DataFrame({'A': [1, None, 3, 3], 'B': [' x ', 'Y', 'z ', 'z ']})

    def test_drop_missing(self):
        cleaned = data_cleaning.drop_missing(self.df)
        self.assertFalse(cleaned.isnull().any().any())
        self.assertEqual(len(cleaned), 3)

    def test_fill_missing(self):
        filled = data_cleaning.fill_missing(self.df, 99)
        self.assertTrue((filled['A'] == 99).any())

    def test_remove_duplicates(self):
        # Add a duplicate row for testing
        df_dup = pd.DataFrame({'A': [1, None, 3, 3], 'B': [' x ', 'Y', 'z ', 'z ']})
        deduped = data_cleaning.remove_duplicates(df_dup)
        self.assertEqual(len(deduped), 3)

    def test_convert_types(self):
        converted = data_cleaning.convert_types(self.df, {'A': 'float64'})
        self.assertEqual(str(converted['A'].dtype), 'float64')

    def test_handle_outliers_clip(self):
        clipped = data_cleaning.handle_outliers(self.df, 'A', 'clip', 1, 2)
        # Only check non-NaN values
        valid = clipped['A'].dropna()
        self.assertTrue(((valid <= 2) & (valid >= 1)).all())

    def test_handle_outliers_remove(self):
        removed = data_cleaning.handle_outliers(self.df, 'A', 'remove', 1, 2)
        self.assertTrue(((removed['A'] <= 2) & (removed['A'] >= 1)).all())

    def test_clean_strings(self):
        cleaned = data_cleaning.clean_strings(self.df.copy(), 'B')
        self.assertTrue(all(cleaned['B'].str.islower()))
        self.assertTrue(all(cleaned['B'].str.strip() == cleaned['B']))

    def test_extract_numbers(self):
        df_num = pd.DataFrame({'C': ['abc123', 'def456', 'no_num']})
        nums = data_cleaning.extract_numbers(df_num, 'C')
        self.assertEqual(list(nums.dropna()), ['123', '456'])

if __name__ == '__main__':
    unittest.main()
