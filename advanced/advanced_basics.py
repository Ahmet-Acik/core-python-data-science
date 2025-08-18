"""
advanced_basics.py
------------------
A step-by-step, advanced Python guide for data science and robust scripting.

This file follows a progressive pedagogy:
    1. Advanced built-ins
    2. Slicing
    3. Copying (shallow vs deep)
    4. Mutability/Immutability
    5. Advanced error handling
    6. Advanced file I/O (CSV, JSON, pandas)
    7. Iterators & custom iterables
    8. Advanced unpacking
    9. Nested/conditional comprehensions
    10. Type hints (typing)
    11. Context managers (class/contextlib)
    12. Regex (groups, match objects, cleaning)
    13. Datetime (parsing, timezones, pandas)
    14. Argparse (CLI)
    15. __main__ block with real-world demos

All examples use type hints, docstrings, and practical comments. See the __main__ block for usage.
"""

from typing import Any, Iterator, List, Dict, Optional, Union
import copy
import logging
import csv, json
import pandas as pd
from contextlib import contextmanager
import re
from datetime import datetime, timezone
import argparse

# 1. ADVANCED BUILT-IN FUNCTIONS
nums: list[int] = [5, 2, 9, 1]
sorted_nums: list[int] = sorted(nums)
reversed_nums: list[int] = list(reversed(nums))
sum_with_start: int = sum(nums, 10)

# 2. SLICING
letters: list[str] = ['a', 'b', 'c', 'd', 'e']
first_three: list[str] = letters[:3]
last_two: list[str] = letters[-2:]
every_other: list[str] = letters[::2]
reversed_letters: list[str] = letters[::-1]

# 3. COPYING (SHALLOW VS DEEP)
original: list[list[int]] = [[1, 2], [3, 4]]
shallow: list[list[int]] = list(original)
deep: list[list[int]] = copy.deepcopy(original)
original[0][0] = 99  # Affects shallow, not deep

# 4. MUTABILITY/IMMUTABILITY
immutable_tuple: tuple[int, ...] = (1, 2, 3)
mutable_list: list[int] = [1, 2, 3]
mutable_list[0] = 10

# 5. ADVANCED ERROR HANDLING
def parse_int(val: Any) -> int | None:
    """
    Try to parse an integer from val. Returns None if ValueError.
    Logs unexpected errors and re-raises them.
    """
    try:
        return int(val)
    except ValueError:
        logging.warning(f"ValueError: {val} is not an int")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise
    else:
        logging.info("Parsed successfully!")
    finally:
        logging.debug("parse_int finished.")

# 6. ADVANCED FILE I/O (CSV, JSON, pandas)
def write_csv(filename: str = 'data.csv') -> None:
    """
    Write sample data to a CSV file.
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'score'])
        writer.writerow(['Alice', 90])
        writer.writerow(['Bob', 85])

def read_csv(filename: str = 'data.csv') -> list[dict[str, str]]:
    """
    Read a CSV file into a list of dicts.
    """
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_csv_pandas(filename: str = 'data.csv') -> pd.DataFrame:
    """
    Read a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(filename)

def write_json(data: dict[str, Any], filename: str = 'data.json') -> None:
    """
    Write a dict to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def read_json(filename: str = 'data.json') -> dict[str, Any]:
    """
    Read a JSON file into a dict.
    """
    with open(filename) as f:
        return json.load(f)

# 7. ITERATORS & CUSTOM ITERABLES
class Counter:
    """
    Custom iterator that counts from low to high (inclusive).
    """
    def __init__(self, low: int, high: int) -> None:
        self.current = low
        self.high = high
    def __iter__(self) -> 'Counter':
        return self
    def __next__(self) -> int:
        if self.current > self.high:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# 8. ADVANCED UNPACKING
head, *body, tail = [1, 2, 3, 4, 5]

# 9. NESTED/CONDITIONAL COMPREHENSIONS
mat: list[list[int]] = [[1,2,3],[4,5,6]]
flat: list[int] = [x for row in mat for x in row]
even_squares: list[int] = [x**2 for x in range(10) if x % 2 == 0]

# 10. TYPE HINTS (typing)
def greet_all(names: List[str]) -> None:
    """Print a greeting for each name."""
    for name in names:
        print(f"Hello, {name}")

def get_value(d: Dict[str, int], key: str) -> Optional[int]:
    """Get value from dict, or None if not found."""
    return d.get(key)

def add_or_concat(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    """
    Add if both are int, concatenate if both are str, else raise TypeError.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError("Arguments must be both int or both str.")

# 11. CONTEXT MANAGERS (__enter__/__exit__, contextlib)
class FileOpener:
    """
    Class-based context manager for opening files.
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename
    def __enter__(self) -> Any:
        self.file = open(self.filename, 'r')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()

@contextmanager
def managed_resource(name: str) -> Iterator[str]:
    """
    Context manager using contextlib.
    """
    print(f"Acquiring {name}")
    yield name
    print(f"Releasing {name}")

# 12. REGEX (groups, match objects, data cleaning)
pattern = r'(\w+)@(\w+)\.com'
match = re.match(pattern, 'test@example.com')
if match:
    user, domain = match.groups()

def clean_phone_numbers(text: str) -> list[str]:
    """
    Extract all phone numbers from text.
    """
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(phone_pattern, text)

# 13. DATETIME (parsing, timezones, time series)
iso_str = '2025-08-18T12:00:00+00:00'
dt = datetime.fromisoformat(iso_str)
now_utc = datetime.now(timezone.utc)

def parse_dates_pandas(series: pd.Series) -> pd.Series:
    """
    Parse a pandas Series of date strings to datetime objects.
    """
    return pd.to_datetime(series)

# 14. ARGPARSE (CLI)
def argparse_advanced() -> argparse.Namespace:
    """
    Example CLI with subcommands. Run from terminal:
    python advanced_basics.py foo --bar 42
    """
    parser = argparse.ArgumentParser(description='Advanced Example')
    subparsers = parser.add_subparsers(dest='command')
    foo_parser = subparsers.add_parser('foo')
    foo_parser.add_argument('--bar', type=int, default=0)
    args = parser.parse_args()
    return args

# 15. EXAMPLE USAGE (REAL-WORLD DEMOS)
if __name__ == "__main__":
    print("\n--- Advanced Built-ins ---")
    print(f"Sorted: {sorted_nums}")
    print(f"Reversed: {reversed_nums}")
    print(f"Sum with start: {sum_with_start}")

    print("\n--- Slicing ---")
    print(f"First three: {first_three}")
    print(f"Last two: {last_two}")
    print(f"Every other: {every_other}")
    print(f"Reversed: {reversed_letters}")

    print("\n--- Shallow vs Deep Copy (Wrong/Right) ---")
    print(f"Original: {original}")
    print(f"Shallow: {shallow}")
    print(f"Deep: {deep}")

    print("\n--- Mutability ---")
    print(f"Tuple (immutable): {immutable_tuple}")
    print(f"List (mutable): {mutable_list}")

    print("\n--- Error Handling ---")
    print(f"parse_int('42'): {parse_int('42')}")
    print(f"parse_int('notanint'): {parse_int('notanint')}")

    print("\n--- File I/O (CSV/JSON) ---")
    write_csv()
    print(f"CSV rows: {read_csv()}")
    import os
    if os.path.exists('data.csv'):
        df = read_csv_pandas()
        print(f"Pandas DataFrame:\n{df}")
    write_json({'a': 1, 'b': 2})
    print(f"JSON: {read_json()}")

    print("\n--- Iterators ---")
    counter = Counter(1, 3)
    print("Counter values:", list(counter))
    for i in Counter(4, 6):
        print(f"Iter: {i}")

    print("\n--- Advanced Unpacking ---")
    print(f"head: {head}, body: {body}, tail: {tail}")

    print("\n--- Comprehensions ---")
    print(f"Flat: {flat}")
    print(f"Even squares: {even_squares}")

    print("\n--- Type Hints ---")
    greet_all(['Alice', 'Bob'])
    print(f"get_value: {get_value({'x': 1}, 'x')}")
    try:
        print(f"add_or_concat(1, 2): {add_or_concat(1, 2)}")
        print(f"add_or_concat('a', 'b'): {add_or_concat('a', 'b')}")
        add_or_concat(1, 'b')
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    print("\n--- Context Managers ---")
    with FileOpener('data.csv') as f:
        print(f"First line of data.csv: {f.readline().strip()}")
    with managed_resource('resource') as r:
        print(f"Using {r}")

    print("\n--- Regex ---")
    if match:
        user, domain = match.groups()
        print(f"Email match: user={user}, domain={domain}")
    else:
        print("No email match found.")
    phones = clean_phone_numbers('Call 555-123-4567 or 555.987.6543!')
    print(f"Phones found: {phones}")

    print("\n--- Datetime ---")
    print(f"Parsed: {dt}, Now UTC: {now_utc}")
    s = pd.Series(['2025-01-01', '2025-08-18'])
    print(f"Parsed dates: {parse_dates_pandas(s)}")

    print("\n--- Argparse (CLI) ---")
    # To test argparse, run: python advanced_basics.py foo --bar 42
    # args = argparse_advanced()
    # print(f"Args: {args}")
