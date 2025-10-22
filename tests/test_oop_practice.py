import unittest
from oop import oop_practice

class TestOOPPractice(unittest.TestCase):
    def test_animal_speak(self):
        a = oop_practice.Animal('Generic')
        self.assertEqual(a.speak(), 'Generic makes a sound.')
        d = oop_practice.Dog('Buddy')
        self.assertEqual(d.speak(), 'Buddy barks.')
        c = oop_practice.Cat('Luna')
        self.assertEqual(c.speak(), 'Luna meows.')

    def test_bank_account(self):
        acct = oop_practice.BankAccount('Alice', 100)
        acct.deposit(50)
        self.assertEqual(acct.get_balance(), 150)
        acct.withdraw(100)
        self.assertEqual(acct.get_balance(), 50)
        with self.assertRaises(ValueError):
            acct.withdraw(100)

    def test_polymorphism(self):
        animals = [oop_practice.Dog('Rex'), oop_practice.Cat('Misty'), oop_practice.Animal('Creature')]
        voices = [a.speak() for a in animals]
        self.assertEqual(voices, ['Rex barks.', 'Misty meows.', 'Creature makes a sound.'])

    def test_vector(self):
        v1 = oop_practice.Vector(1, 2)
        v2 = oop_practice.Vector(3, 4)
        v3 = v1 + v2
        self.assertEqual(v3, oop_practice.Vector(4, 6))
        self.assertEqual(repr(v3), 'Vector(4, 6)')
        self.assertTrue(v1 == oop_practice.Vector(1, 2))
        self.assertFalse(v1 == v2)

    def test_mathutils(self):
        self.assertEqual(oop_practice.MathUtils.add(2, 3), 5)
        self.assertEqual(oop_practice.MathUtils.identity(), 'MathUtils')

    def test_rectangle_area(self):
        rect = oop_practice.Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_point_dataclass(self):
        p = oop_practice.Point(1.5, 2.5)
        self.assertEqual(p.x, 1.5)
        self.assertEqual(p.y, 2.5)

    def test_employee_manager(self):
        emp = oop_practice.Employee('Bob', 50000)
        emp.give_raise(5000)
        self.assertEqual(emp.salary, 55000)
        self.assertEqual(str(emp), 'Bob: $55000.00')
        mgr = oop_practice.Manager('Sue', 70000)
        mgr.add_report(emp)
        self.assertIn('Bob', str(mgr))
        self.assertEqual(mgr.salary, 70000)
        self.assertEqual(mgr.reports[0].name, 'Bob')

if __name__ == "__main__":
    unittest.main()
