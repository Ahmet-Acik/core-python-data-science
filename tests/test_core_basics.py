import unittest
import os
from basics import core_basics

class TestCoreBasics(unittest.TestCase):
    def test_variables_and_types(self):
        self.assertIsInstance(core_basics.age, int)
        self.assertIsInstance(core_basics.height, float)
        self.assertIsInstance(core_basics.name, str)
        self.assertIsInstance(core_basics.is_student, bool)
        self.assertIsNone(core_basics.nothing)

    def test_basic_operations(self):
        self.assertEqual(core_basics.total, 100)
        self.assertTrue(core_basics.is_high_score)
        self.assertEqual(core_basics.diff, 85)
        self.assertEqual(core_basics.exp, 8)

    def test_lists_tuples_sets_dicts(self):
        self.assertIn("pear", core_basics.fruits)
        self.assertEqual(core_basics.colors, ("red", "green", "blue"))
        self.assertIn("apple", core_basics.unique_fruits)
        self.assertEqual(core_basics.person["city"], "Izmir")
        self.assertEqual(core_basics.nums_dict["a"], 1)

    def test_control_flow(self):
        self.assertIn(core_basics.result, ["Excellent", "Good", "Needs improvement"])
        self.assertEqual(core_basics.find_first_long_word(["hi", "hello", "world"], 5), "hello")
        self.assertEqual(core_basics.count_down(3), [3, 2, 1])

    def test_functions_and_lambdas(self):
        self.assertEqual(core_basics.greet("Ada"), "Hi, Ada!")
        self.assertEqual(core_basics.add(2, 3), 5)
        self.assertEqual(core_basics.square(4), 16)

    def test_comprehensions(self):
        self.assertEqual(core_basics.lengths, [len(f) for f in core_basics.fruits])
        self.assertEqual(core_basics.fruit_map["apple"], 5)
        self.assertTrue(all(isinstance(x, int) for x in core_basics.lengths))

    def test_string_list_dict_methods(self):
        self.assertEqual(core_basics.clean, core_basics.sentence.strip())
        self.assertEqual(core_basics.joined, ":".join(core_basics.words))
        self.assertEqual(core_basics.replaced, "Data is fun!")
        self.assertIn(7, core_basics.nums)
        self.assertGreaterEqual(core_basics.count_2, 0)
        self.assertGreaterEqual(core_basics.index_9, -1)

    def test_functional_tools(self):
        self.assertTrue(all(x % 2 == 0 for x in core_basics.evens))
        self.assertTrue(all(x == y**2 for x, y in zip(core_basics.squares, core_basics.nums)))
        self.assertTrue(core_basics.all_positive)
        self.assertTrue(core_basics.any_even)

    def test_exception_handling(self):
        self.assertEqual(core_basics.safe_divide(10, 2), 5)
        self.assertEqual(core_basics.safe_divide(10, 0), 'Cannot divide by zero')

    def test_file_io(self):
        content = core_basics.write_and_read_temp()
        self.assertIn('Temporary data!', content)
        os.remove('tempfile.txt')

    def test_decorators_and_generators(self):
        self.assertEqual(core_basics.say_hi("Test"), "Hi, Test!")
        self.assertEqual(list(core_basics.countdown_gen(3)), [3, 2, 1])

    def test_type_annotations(self):
        types = core_basics.type_overview()
        self.assertIsInstance(types, dict)
        self.assertIn('score', types)
        self.assertEqual(types['score'], int)

    def test_regex_and_datetime(self):
        self.assertEqual(core_basics.extract_year('Conference 2025'), '2025')
        start, end = core_basics.week_range()
        self.assertIsInstance(start, str)
        self.assertIsInstance(end, str)

    def test_argparse(self):
        self.assertEqual(core_basics.parse_cli(), 2)

if __name__ == "__main__":
    unittest.main()
