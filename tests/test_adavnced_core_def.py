import unittest
import pandas as pd
import numpy as np
from advanced import adavnced_core_def

class TestAdvancedCoreDef(unittest.TestCase):
    def test_demo_advanced_builtins(self):
        # Just check that it runs without error
        adavnced_core_def.demo_advanced_builtins()

    def test_demo_slicing(self):
        df = adavnced_core_def.demo_slicing()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertListEqual(list(df.columns), ['A', 'B'])

    def test_demo_copying(self):
        df = pd.DataFrame({'A': range(5), 'B': range(5,10)})
        adavnced_core_def.demo_copying(df)
        # Check that original df is not mutated at index 0
        self.assertEqual(df.loc[0, 'A'], 0)

    def test_demo_sets(self):
        adavnced_core_def.demo_sets()

    def test_demo_custom_exceptions(self):
        adavnced_core_def.demo_custom_exceptions()

    def test_demo_fileio_gzip_excel(self):
        df = pd.DataFrame({'A': range(5), 'B': range(5,10)})
        adavnced_core_def.demo_fileio_gzip_excel(df)

    def test_demo_generators_itertools(self):
        adavnced_core_def.demo_generators_itertools()

    def test_demo_dict_unpacking(self):
        adavnced_core_def.demo_dict_unpacking()

    def test_demo_comprehensions(self):
        adavnced_core_def.demo_comprehensions()

    def test_demo_typing(self):
        adavnced_core_def.demo_typing()

if __name__ == '__main__':
    unittest.main()
