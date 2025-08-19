"""
oop_patterns.py
----------------
Grouped, practical OOP patterns and advanced concepts for Python.
Covers: Design Patterns, SOLID, Mixins, Composition, Properties, Custom Exceptions, Protocols, Unit Testing, Serialization, Metaclasses, and OOP in Data Science.
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol
from dataclasses import dataclass
import pickle
import json

# 1. DESIGN PATTERNS
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class Product(ABC):
    @abstractmethod
    def use(self) -> str:
        pass
class ConcreteProductA(Product):
    def use(self) -> str:
        return "ProductA used"
class ConcreteProductB(Product):
    def use(self) -> str:
        return "ProductB used"
class Factory:
    def create(self, kind: str) -> Product:
        if kind == 'A':
            return ConcreteProductA()
        elif kind == 'B':
            return ConcreteProductB()
        else:
            raise ValueError('Unknown kind')

# 2. SOLID PRINCIPLES
class OpenClosedShape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
class OCSquare(OpenClosedShape):
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return self.side ** 2
class OCCircle(OpenClosedShape):
    def __init__(self, r: float):
        self.r = r
    def area(self) -> float:
        return 3.14 * self.r ** 2

# 3. MIXINS & MULTIPLE INHERITANCE
class JsonMixin:
    def to_json(self) -> str:
        return json.dumps(self.__dict__)
class PrintableMixin:
    def print_info(self):
        print(self.__dict__)
class User(JsonMixin, PrintableMixin):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# 4. COMPOSITION VS INHERITANCE
class Engine:
    def start(self):
        return "Engine started"
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        return self.engine.start() + ", Car is moving"

# 5. PROPERTY DECORATORS
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

# 6. CUSTOM EXCEPTIONS
class ValidationError(Exception):
    pass
class Person:
    def __init__(self, name: str, age: int):
        if age < 0:
            raise ValidationError("Age cannot be negative")
        self.name = name
        self.age = age

# 7. PROTOCOLS (Typing)
class Flyer(Protocol):
    def fly(self) -> str: ...
class Bird:
    def fly(self) -> str:
        return "Bird flies"
class Plane:
    def fly(self) -> str:
        return "Plane flies"
def make_it_fly(f: Flyer):
    return f.fly()

# 8. UNIT TESTING (with simple asserts)
class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
    def mul(self, a: int, b: int) -> int:
        return a * b

def test_calculator():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.mul(2, 3) == 6

# 9. SERIALIZATION
@dataclass
class DataPoint:
    x: float
    y: float

def serialize_pickle(obj: Any, filename: str):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
def deserialize_pickle(filename: str) -> Any:
    with open(filename, 'rb') as f:
        return pickle.load(f)

def serialize_json(obj: Any, filename: str):
    with open(filename, 'w') as f:
        json.dump(obj.__dict__, f)
def deserialize_json(filename: str) -> dict:
    with open(filename) as f:
        return json.load(f)

# 10. METACLASSES
class UpperAttrMeta(type):
    def __new__(cls, name, bases, dct):
        attrs = {k.upper() if not (k.startswith('__') and k.endswith('__')) else k: v for k, v in dct.items()}
        return super().__new__(cls, name, bases, attrs)
class Foo(metaclass=UpperAttrMeta):
    bar = 'baz'

# 11. OOP IN DATA SCIENCE
from typing import TypeVar, Generic

Self = TypeVar("Self", bound="Transformer")

class Transformer(ABC):
    @abstractmethod
    def fit(self: Self, X) -> Self: ...
    @abstractmethod
    def transform(self, X) -> list[float]: ...
class StandardScalerDS(Transformer):
    def fit(self, X):
        self.mean = sum(X) / len(X)
        self.std = (sum((x - self.mean) ** 2 for x in X) / len(X)) ** 0.5
        return self
    def transform(self, X):
        return [(x - self.mean) / self.std for x in X]

if __name__ == "__main__":
    print("--- Design Patterns ---")
    s1 = Singleton()
    s2 = Singleton()
    print("Singleton same instance:", s1 is s2)
    f = Factory()
    print(f.create('A').use())
    print(f.create('B').use())

    print("\n--- SOLID ---")
    shapes = [OCSquare(2), OCCircle(1)]
    print([s.area() for s in shapes])

    print("\n--- Mixins ---")
    u = User("Alice", 30)
    u.print_info()
    print(u.to_json())

    print("\n--- Composition ---")
    car = Car()
    print(car.drive())

    print("\n--- Property Decorators ---")
    t = Temperature(25)
    print(t.celsius, t.fahrenheit)
    t.celsius = 0
    print(t.celsius, t.fahrenheit)

    print("\n--- Custom Exceptions ---")
    try:
        p = Person("Bob", -1)
    except ValidationError as e:
        print(e)

    print("\n--- Protocols ---")
    print(make_it_fly(Bird()))
    print(make_it_fly(Plane()))

    print("\n--- Unit Testing ---")
    test_calculator()
    print("Calculator tests passed.")

    print("\n--- Serialization ---")
    dp = DataPoint(1.0, 2.0)
    serialize_pickle(dp, 'datapoint.pkl')
    print(deserialize_pickle('datapoint.pkl'))
    serialize_json(dp, 'datapoint.json')
    print(deserialize_json('datapoint.json'))

    print("\n--- Metaclasses ---")
    print(hasattr(Foo, 'BAR'))
    print(Foo.BAR)

    print("\n--- OOP in Data Science ---")
    scaler = StandardScalerDS().fit([1, 2, 3, 4, 5])
    print(scaler.transform([1, 2, 3, 4, 5]))
