import unittest
import pandas as pd
import json
import os
import sqlite3
from data_science import data_loading

class TestDataLoading(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data_loading.create_sample_data()

    def test_load_csv(self):
        df = data_loading.load_csv('datasets/sample.csv')
        self.assertEqual(list(df.columns), ['name', 'age', 'city'])
        self.assertEqual(len(df), 3)

    def test_load_json(self):
        data = data_loading.load_json('datasets/sample.json')
        self.assertIn('users', data)
        self.assertEqual(data['users'][0]['name'], 'Alice')

    def test_load_sqlite(self):
        df = data_loading.load_sqlite('datasets/sample.db', 'SELECT * FROM users')
        self.assertEqual(list(df.columns), ['name', 'age', 'city'])
        self.assertEqual(len(df), 3)

    def test_save_csv(self):
        df = pd.DataFrame({'x': [1,2], 'y': [3,4]})
        data_loading.save_csv(df, 'datasets/test.csv')
        loaded = pd.read_csv('datasets/test.csv')
        self.assertTrue((loaded == df).all().all())
        os.remove('datasets/test.csv')

    def test_save_json(self):
        obj = {'a': 1, 'b': 2}
        data_loading.save_json(obj, 'datasets/test.json')
        with open('datasets/test.json') as f:
            loaded = json.load(f)
        self.assertEqual(loaded, obj)
        os.remove('datasets/test.json')

    def test_fetch_api(self):
        data = data_loading.fetch_api('https://jsonplaceholder.typicode.com/posts/1')
        self.assertIn('title', data)
        self.assertIn('body', data)

if __name__ == '__main__':
    unittest.main()
