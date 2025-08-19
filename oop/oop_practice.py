"""
oop_practice.py
---------------
Comprehensive, step-by-step OOP practice for Python.
Covers: classes, attributes, methods, inheritance, polymorphism, encapsulation, dunder methods, class/static methods, abstract base classes, dataclasses, and real-world examples.
"""

from abc import ABC, abstractmethod
from typing import Any
from dataclasses import dataclass

# 1. BASIC CLASS & INSTANCE
class Animal:
    """A simple Animal class."""
    def __init__(self, name: str):
        self.name = name
    def speak(self) -> str:
        return f"{self.name} makes a sound."

# 2. INHERITANCE
class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} meows."

# 3. ENCAPSULATION
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance  # protected
    def deposit(self, amount: float):
        self._balance += amount
    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
    def get_balance(self) -> float:
        return self._balance

# 4. POLYMORPHISM
animals = [Dog("Rex"), Cat("Misty"), Animal("Creature")]
voices = [a.speak() for a in animals]

# 5. DUNDER METHODS
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

# 6. CLASS & STATIC METHODS
class MathUtils:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    @classmethod
    def identity(cls) -> str:
        return cls.__name__

# 7. ABSTRACT BASE CLASSES
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h
    def area(self) -> float:
        return self.w * self.h

# 8. DATACLASSES
@dataclass
class Point:
    x: float
    y: float

# 9. REAL-WORLD EXAMPLE: EMPLOYEE SYSTEM
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    def give_raise(self, amount: float):
        self.salary += amount
    def __str__(self):
        return f"{self.name}: ${self.salary:.2f}"

class Manager(Employee):
    def __init__(self, name: str, salary: float, reports: list[Employee] = None):
        super().__init__(name, salary)
        self.reports = reports or []
    def add_report(self, emp: Employee):
        self.reports.append(emp)
    def __str__(self):
        return f"Manager {self.name}: ${self.salary:.2f}, Reports: {[e.name for e in self.reports]}"

if __name__ == "__main__":
    print("--- OOP Practice ---")
    a = Animal("Generic")
    d = Dog("Buddy")
    c = Cat("Luna")
    print(a.speak())
    print(d.speak())
    print(c.speak())

    acct = BankAccount("Alice", 100)
    acct.deposit(50)
    try:
        acct.withdraw(200)
    except ValueError as e:
        print(e)
    print("Balance:", acct.get_balance())

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print("v1 + v2:", v1 + v2)
    print("v1 == v2:", v1 == v2)

    print("MathUtils.add:", MathUtils.add(2, 3))
    print("MathUtils.identity:", MathUtils.identity())

    rect = Rectangle(3, 4)
    print("Rectangle area:", rect.area())

    p = Point(1.5, 2.5)
    print("Point:", p)

    emp = Employee("Bob", 50000)
    mgr = Manager("Sue", 70000)
    mgr.add_report(emp)
    print(emp)
    print(mgr)
    print("Polymorphism voices:", voices)
