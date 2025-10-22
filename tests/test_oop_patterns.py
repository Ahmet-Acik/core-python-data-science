import unittest
import os
from oop import oop_patterns

class TestOOPPatterns(unittest.TestCase):
    def test_singleton(self):
        s1 = oop_patterns.Singleton()
        s2 = oop_patterns.Singleton()
        self.assertIs(s1, s2)

    def test_factory(self):
        f = oop_patterns.Factory()
        self.assertEqual(f.create('A').use(), 'ProductA used')
        self.assertEqual(f.create('B').use(), 'ProductB used')
        with self.assertRaises(ValueError):
            f.create('C')

    def test_solid(self):
        square = oop_patterns.OCSquare(2)
        circle = oop_patterns.OCCircle(1)
        self.assertAlmostEqual(square.area(), 4)
        self.assertAlmostEqual(circle.area(), 3.14)

    def test_mixins(self):
        u = oop_patterns.User('Alice', 30)
        self.assertEqual(u.to_json(), '{"name": "Alice", "age": 30}')
        # PrintableMixin prints info, just check no error
        u.print_info()

    def test_composition(self):
        car = oop_patterns.Car()
        self.assertIn('Engine started', car.drive())
        self.assertIn('Car is moving', car.drive())

    def test_property_decorators(self):
        t = oop_patterns.Temperature(25)
        self.assertEqual(t.celsius, 25)
        self.assertAlmostEqual(t.fahrenheit, 77)
        t.celsius = 0
        self.assertEqual(t.celsius, 0)
        with self.assertRaises(ValueError):
            t.celsius = -300

    def test_custom_exceptions(self):
        with self.assertRaises(oop_patterns.ValidationError):
            oop_patterns.Person('Bob', -1)
        p = oop_patterns.Person('Alice', 20)
        self.assertEqual(p.name, 'Alice')
        self.assertEqual(p.age, 20)

    def test_protocols(self):
        self.assertEqual(oop_patterns.make_it_fly(oop_patterns.Bird()), 'Bird flies')
        self.assertEqual(oop_patterns.make_it_fly(oop_patterns.Plane()), 'Plane flies')

    def test_calculator(self):
        calc = oop_patterns.Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.mul(2, 3), 6)

    def test_serialization(self):
        dp = oop_patterns.DataPoint(1.0, 2.0)
        oop_patterns.serialize_pickle(dp, 'datapoint.pkl')
        dp2 = oop_patterns.deserialize_pickle('datapoint.pkl')
        self.assertEqual(dp2.x, 1.0)
        self.assertEqual(dp2.y, 2.0)
        oop_patterns.serialize_json(dp, 'datapoint.json')
        dp3 = oop_patterns.deserialize_json('datapoint.json')
        self.assertEqual(dp3['x'], 1.0)
        self.assertEqual(dp3['y'], 2.0)
        os.remove('datapoint.pkl')
        os.remove('datapoint.json')

    def test_metaclasses(self):
        self.assertTrue(hasattr(oop_patterns.Foo, 'BAR'))
        self.assertEqual(getattr(oop_patterns.Foo, 'BAR'), 'baz')

    def test_oop_data_science(self):
        scaler = oop_patterns.StandardScalerDS().fit([1, 2, 3, 4, 5])
        transformed = scaler.transform([1, 2, 3, 4, 5])
        self.assertAlmostEqual(transformed[0], -1.414213562373095)
        self.assertAlmostEqual(transformed[-1], 1.414213562373095)

if __name__ == "__main__":
    unittest.main()
