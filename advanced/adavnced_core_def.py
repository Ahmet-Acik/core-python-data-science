"""
advanced_basics_plus.py
-----------------------
Advanced Python for data science and scripting: extended edition.

Requirements:
    - Python 3.8+
    - pandas, numpy, openpyxl (for Excel I/O), xlsxwriter (optional), matplotlib (for plotting, if added)

Table of Contents:
    1. Advanced Built-ins
    2. Slicing with numpy and pandas
    3. Copying with pandas DataFrames
    4. Sets and frozensets
    5. Custom exceptions and exception chaining
    6. File I/O with gzip and Excel
    7. Generator functions and itertools
    8. Dict unpacking and function call unpacking
    9. Set and dict comprehensions
    10. TypedDict, Literal, Protocol (typing)
    11. contextlib.suppress, redirect_stdout
    12. Regex: sub, split, lookahead/lookbehind
    13. Datetime: timedelta, timezones
    14. Argparse: mutually exclusive, required, groups
    15. OOP: dataclasses, Singleton, Factory
    16. functools.partial, lru_cache, operator
    17. Unit testing with unittest
    18. Logging config
    19. Performance: timeit, cProfile
    20. Parallelism: concurrent.futures, multiprocessing, asyncio

All examples are practical and ready to run.
"""

import os
import sys
import csv
import json
import gzip
import logging
import timeit
import cProfile
import asyncio
import multiprocessing
from typing import Any, Iterator, List, Dict, Optional, Union, TypedDict, Literal, Protocol
from functools import reduce, partial, lru_cache
from operator import add, mul
from contextlib import contextmanager, suppress, redirect_stdout
import pandas as pd
import numpy as np
import re
from datetime import datetime, timedelta, timezone
import argparse
import itertools
import tempfile


# --- DEMO FUNCTIONS ---
def demo_advanced_builtins():
    """
    Demonstrates advanced built-in functions in Python.
    Covers: any, all, zip, enumerate, map, filter, reduce
    """
    nums = [1, 2, 3, 4, 5]
    print("any >3:", any(x > 3 for x in nums))
    print("all >0:", all(x > 0 for x in nums))
    print("zip:", list(zip([1,2], ['a','b'])))
    print("enumerate:", list(enumerate(['x','y','z'])))
    print("map:", list(map(str, nums)))
    print("filter:", list(filter(lambda x: x % 2 == 0, nums)))
    print("reduce (sum):", reduce(add, nums))


def demo_slicing():
    """Demonstrates slicing with numpy and pandas.

    Returns:
        pd.DataFrame: A sample DataFrame.
    """
    arr = np.arange(10)
    print("numpy slice:", arr[2:7:2])
    df = pd.DataFrame({'A': range(5), 'B': range(5,10)})
    print("pandas iloc:", df.iloc[1:4])
    print("pandas loc:", df.loc[1:3])
    return df


def demo_copying(df):
    """Demonstrates copying DataFrames in pandas.

    Args:
        df (pd.DataFrame): The original DataFrame to copy.
    """
    df2 = df.copy()
    df2.loc[0, 'A'] = 99
    print("Original DataFrame:\n", df)
    print("Copied DataFrame:\n", df2)


def demo_sets():
    """Demonstrates the use of sets and frozensets in Python.
    """
    s = set([1,2,3,2])
    fs = frozenset([4,5,6])
    print("set:", s)
    print("frozenset:", fs)

    
def demo_custom_exceptions():
    """Demonstrates custom exceptions and exception chaining in Python.
    """
    class MyError(Exception): pass
    try:
        try:
            raise ValueError("Inner error")
        except ValueError as e:
            raise MyError("Outer error") from e
    except MyError as e:
        print("Exception chaining:", e)


def demo_fileio_gzip_excel(df):
    """Demonstrates file I/O with GZIP and Excel in Python.
    """
    # GZIP file I/O with cleanup
    gz_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix='.gz', delete=False) as tmp_gz:
            gz_path = tmp_gz.name
        with gzip.open(gz_path, 'wt') as f:
            f.write('hello gzip')
        with gzip.open(gz_path, 'rt') as f:
            print("gzip read:", f.read())
    finally:
        if gz_path and os.path.exists(gz_path):
            os.remove(gz_path)

    # Excel file I/O with cleanup and error handling
    xlsx_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp_xlsx:
            xlsx_path = tmp_xlsx.name
        df.to_excel(xlsx_path)
        try:
            print("Excel read:\n", pd.read_excel(xlsx_path))
        except ImportError as e:
            print("Excel read failed: openpyxl or xlsxwriter may not be installed.", e)
        except Exception as e:
            print("Excel read failed:", e)
    finally:
        if xlsx_path and os.path.exists(xlsx_path):
            os.remove(xlsx_path)


def demo_generators_itertools():
    """Demonstrates generators and itertools in Python.
    """
    def gen():
        for i in range(3):
            yield i*i
    print("generator:", list(gen()))
    print("itertools.cycle:", list(itertools.islice(itertools.cycle([1,2]), 5)))
    print("itertools.permutations:", list(itertools.permutations([1,2,3], 2)))
    

def demo_dict_unpacking():
    """Demonstrates dictionary unpacking in function calls.
    """
    d = {'x': 1, 'y': 2}
    def foo(x, y): return x + y
    print("dict unpacking:", foo(**d))
    print("function call unpacking:", foo(1, *(2,)))
    print("mixed unpacking:", foo(*(1, 2)))
    
    
def demo_comprehensions():
    """Demonstrates set and dictionary comprehensions in Python.
    """
    set_comp = {x**2 for x in range(5)}
    dict_comp = {x: x**2 for x in range(5)}
    print("set comp:", set_comp)
    print("dict comp:", dict_comp)
    

def demo_typing():
    """Demonstrates type hints and annotations in Python.
    """
    class Point(TypedDict):
        x: int
        y: int
    def move(p: Point, dx: int, dy: int) -> Point:
        return {'x': p['x']+dx, 'y': p['y']+dy}
    print("TypedDict:", move({'x':1,'y':2}, 3, 4))
    def foo_lit(x: Literal['a','b']) -> str:
        return f"got {x}"
    print("Literal:", foo_lit('a'))
    class SupportsLen(Protocol):
        def __len__(self) -> int: ...
    def length(obj: SupportsLen) -> int:
        return len(obj)
    print("Protocol:", length([1,2,3]))


def demo_contextlib():
    """Demonstrates contextlib usage in Python.
    """
    with suppress(FileNotFoundError):
        os.remove('no_such_file.txt')
    with open('out.txt', 'w') as f, redirect_stdout(f):
        print("redirected to file")
    print("redirected file content:", open('out.txt').read())


def demo_regex():
    """Demonstrates regular expressions in Python.
    """
    s = "foo123bar456baz"
    print("re.sub:", re.sub(r'\d+', '#', s))
    print("re.split:", re.split(r'\d+', s))
    lookahead = re.findall(r'\w+(?=\d+)', s)
    lookbehind = re.findall(r'(?<=\d)\w+', s)  # Fixed-width look-behind
    print("lookahead:", lookahead)
    print("lookbehind:", lookbehind)
    

def demo_datetime():
    """Demonstrates datetime manipulation in Python.
    """
    dt = datetime(2025, 8, 24, 12, 0, tzinfo=timezone.utc)
    print("timedelta:", dt + timedelta(days=5))
    print("timezone:", dt.astimezone(timezone(timedelta(hours=3))))
    print("datetime:", dt)
    print("datetime (naive):", dt.replace(tzinfo=None))
    print("datetime (UTC):", dt.astimezone(timezone.utc))
    print("datetime (local):", dt.astimezone())
    print("datetime (offset):", dt.astimezone(timezone(timedelta(hours=5))))
    print("datetime (custom):", dt.astimezone(timezone(timedelta(hours=-3))))
    print("datetime (fixed):", dt.astimezone(timezone(timedelta(hours=0))))



def demo_argparse():
    """Demonstrates argparse usage in Python.
    """
    def argparse_demo():
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--foo', action='store_true')
        group.add_argument('--bar', action='store_true')
        parser.add_argument('--baz', type=int, required=True)
        # args = parser.parse_args()
        # print(args)
    print("Argparse demo function defined (not called).")
