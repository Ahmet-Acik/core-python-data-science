import unittest
import pandas as pd
import numpy as np
from advanced import advanced_basics_plus

class TestAdvancedBasicsPlus(unittest.TestCase):
    def test_builtins(self):
        self.assertTrue(any(x > 3 for x in advanced_basics_plus.nums))
        self.assertTrue(all(x > 0 for x in advanced_basics_plus.nums))
        self.assertEqual(list(zip([1,2], ['a','b'])), [(1, 'a'), (2, 'b')])
        self.assertEqual(list(map(str, advanced_basics_plus.nums)), ['1','2','3','4','5'])

    def test_numpy_pandas_slicing(self):
        arr = np.arange(10)
        self.assertTrue(np.array_equal(advanced_basics_plus.arr[2:7:2], np.array([2,4,6])))
        self.assertIsInstance(advanced_basics_plus.df, pd.DataFrame)
        self.assertListEqual(list(advanced_basics_plus.df.columns), ['A', 'B'])

    def test_copying(self):
        df2 = advanced_basics_plus.df.copy()
        df2['A'][0] = 99
        self.assertEqual(advanced_basics_plus.df['A'][0], 0)

    def test_sets_frozensets(self):
        self.assertIsInstance(advanced_basics_plus.s, set)
        self.assertIsInstance(advanced_basics_plus.fs, frozenset)

    def test_dict_unpacking(self):
        self.assertEqual(advanced_basics_plus.foo(**advanced_basics_plus.d), 3)

    def test_set_dict_comprehensions(self):
        self.assertEqual(advanced_basics_plus.set_comp, {0, 1, 4, 9, 16})
        self.assertEqual(advanced_basics_plus.dict_comp, {0: 0, 1: 1, 2: 4, 3: 9, 4: 16})

    def test_typeddict_literal_protocol(self):
        p = advanced_basics_plus.Point(x=1, y=2)
        moved = advanced_basics_plus.move(p, 3, 4)
        self.assertEqual(moved, {'x':4,'y':6})
        self.assertEqual(advanced_basics_plus.foo_lit('a'), 'got a')
        self.assertEqual(advanced_basics_plus.length([1,2,3]), 3)

    def test_dataclass_singleton_factory(self):
        person = advanced_basics_plus.Person('Alice', 30)
        self.assertEqual(person.name, 'Alice')
        self.assertEqual(person.age, 30)
        s1 = advanced_basics_plus.Singleton()
        s2 = advanced_basics_plus.Singleton()
        self.assertIs(s1, s2)
        dog = advanced_basics_plus.animal_factory('dog')
        self.assertEqual(type(dog).__name__, 'Dog')

    def test_partial_lru_operator(self):
        pow2_3 = advanced_basics_plus.partial(advanced_basics_plus.pow2, 2)
        self.assertEqual(pow2_3(5), 32)
        self.assertEqual(advanced_basics_plus.fib(10), 55)
        self.assertEqual(advanced_basics_plus.mul(3, 4), 12)

if __name__ == '__main__':
    unittest.main()
