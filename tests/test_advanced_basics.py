import unittest
import pandas as pd
import os
from advanced import advanced_basics

class TestAdvancedBasics(unittest.TestCase):
    def test_builtins(self):
        self.assertEqual(advanced_basics.sorted_nums, sorted(advanced_basics.nums))
        self.assertEqual(advanced_basics.reversed_nums, list(reversed(advanced_basics.nums)))
        self.assertEqual(advanced_basics.sum_with_start, sum(advanced_basics.nums) + 10)

    def test_slicing(self):
        self.assertEqual(advanced_basics.first_three, ['a', 'b', 'c'])
        self.assertEqual(advanced_basics.last_two, ['d', 'e'])
        self.assertEqual(advanced_basics.every_other, ['a', 'c', 'e'])
        self.assertEqual(advanced_basics.reversed_letters, ['e', 'd', 'c', 'b', 'a'])

    def test_copying(self):
        self.assertEqual(advanced_basics.shallow[0][0], 99)
        self.assertEqual(advanced_basics.deep[0][0], 1)

    def test_mutability(self):
        self.assertEqual(advanced_basics.immutable_tuple, (1, 2, 3))
        self.assertEqual(advanced_basics.mutable_list[0], 10)

    def test_parse_int(self):
        self.assertEqual(advanced_basics.parse_int('42'), 42)
        self.assertIsNone(advanced_basics.parse_int('notanint'))

    def test_fileio(self):
        advanced_basics.write_csv('test_data.csv')
        rows = advanced_basics.read_csv('test_data.csv')
        self.assertEqual(rows[0]['name'], 'Alice')
        df = advanced_basics.read_csv_pandas('test_data.csv')
        self.assertEqual(list(df.columns), ['name', 'score'])
        advanced_basics.write_json({'a': 1}, 'test_data.json')
        data = advanced_basics.read_json('test_data.json')
        self.assertEqual(data['a'], 1)
        os.remove('test_data.csv')
        os.remove('test_data.json')

    def test_counter(self):
        c = advanced_basics.Counter(1, 3)
        self.assertEqual(list(c), [1, 2, 3])

    def test_unpacking(self):
        self.assertEqual(advanced_basics.head, 1)
        self.assertEqual(advanced_basics.body, [2, 3, 4])
        self.assertEqual(advanced_basics.tail, 5)

    def test_comprehensions(self):
        self.assertEqual(advanced_basics.flat, [1,2,3,4,5,6])
        self.assertEqual(advanced_basics.even_squares, [0,4,16,36,64])

    def test_type_hints(self):
        self.assertEqual(advanced_basics.get_value({'x': 1}, 'x'), 1)
        self.assertEqual(advanced_basics.add_or_concat(1, 2), 3)
        self.assertEqual(advanced_basics.add_or_concat('a', 'b'), 'ab')
        with self.assertRaises(TypeError):
            advanced_basics.add_or_concat(1, 'b')

    def test_context_managers(self):
        advanced_basics.write_csv('test_data.csv')
        with advanced_basics.FileOpener('test_data.csv') as f:
            self.assertEqual(f.readline().strip(), 'name,score')
        with advanced_basics.managed_resource('test_resource') as r:
            self.assertEqual(r, 'test_resource')
        os.remove('test_data.csv')

    def test_regex(self):
        self.assertEqual(advanced_basics.user, 'test')
        self.assertEqual(advanced_basics.domain, 'example')
        phones = advanced_basics.clean_phone_numbers('Call 555-123-4567 or 555.987.6543!')
        self.assertIn('555-123-4567', phones)
        self.assertIn('555.987.6543', phones)

    def test_datetime(self):
        self.assertEqual(advanced_basics.dt.year, 2025)
        self.assertEqual(advanced_basics.now_utc.tzinfo, advanced_basics.timezone.utc)
        s = pd.Series(['2025-01-01', '2025-08-18'])
        parsed = advanced_basics.parse_dates_pandas(s)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(parsed))

if __name__ == '__main__':
    unittest.main()
