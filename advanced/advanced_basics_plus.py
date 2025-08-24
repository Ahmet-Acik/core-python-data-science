"""
advanced_basics_plus.py
-----------------------
Advanced Python for data science and scripting: extended edition.

This file adds to advanced_basics.py with:
    - More built-ins (any, all, zip, enumerate, map, filter, reduce)
    - Slicing with numpy and pandas
    - Copying with pandas DataFrames
    - Sets and frozensets
    - Custom exceptions and exception chaining
    - File I/O with gzip and Excel
    - Generator functions and itertools
    - Dict unpacking and function call unpacking
    - Set and dict comprehensions
    - TypedDict, Literal, Protocol (typing)
    - contextlib.suppress, redirect_stdout
    - Regex: sub, split, lookahead/lookbehind
    - Datetime: timedelta, timezones
    - Argparse: mutually exclusive, required, groups
    - OOP: dataclasses, Singleton, Factory
    - functools.partial, lru_cache, operator
    - Unit testing with unittest
    - Logging config
    - Performance: timeit, cProfile
    - Parallelism: concurrent.futures, multiprocessing, asyncio

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

# --- ADVANCED BUILT-INS ---
nums = [1, 2, 3, 4, 5]
print("any >3:", any(x > 3 for x in nums))
print("all >0:", all(x > 0 for x in nums))
print("zip:", list(zip([1,2], ['a','b'])))
print("enumerate:", list(enumerate(['x','y','z'])))
print("map:", list(map(str, nums)))
print("filter:", list(filter(lambda x: x % 2 == 0, nums)))
print("reduce (sum):", reduce(add, nums))

# --- SLICING WITH NUMPY/PANDAS ---
arr = np.arange(10)
print("numpy slice:", arr[2:7:2])
df = pd.DataFrame({'A': range(5), 'B': range(5,10)})
print("pandas iloc:", df.iloc[1:4])
print("pandas loc:", df.loc[1:3])

# --- COPYING WITH PANDAS ---
df2 = df.copy()
df2['A'][0] = 99
print("Original DataFrame:\n", df)
print("Copied DataFrame:\n", df2)

# --- SETS AND FROZENSETS ---
s = set([1,2,3,2])
fs = frozenset([4,5,6])
print("set:", s)
print("frozenset:", fs)

# --- CUSTOM EXCEPTIONS & CHAINING ---
class MyError(Exception): pass
try:
    try:
        raise ValueError("Inner error")
    except ValueError as e:
        raise MyError("Outer error") from e
except MyError as e:
    print("Exception chaining:", e)
    
import tempfile

# --- FILE I/O WITH GZIP & EXCEL ---
with tempfile.NamedTemporaryFile(suffix='.gz', delete=False) as tmp_gz:
    gz_path = tmp_gz.name
with gzip.open(gz_path, 'wt') as f:
    f.write('hello gzip')
with gzip.open(gz_path, 'rt') as f:
    print("gzip read:", f.read())
os.remove(gz_path)

with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp_xlsx:
    xlsx_path = tmp_xlsx.name
df.to_excel(xlsx_path)
print("Excel read:\n", pd.read_excel(xlsx_path))
os.remove(xlsx_path)


# --- GENERATORS & ITERTOOLS ---
def gen():
    for i in range(3):
        yield i*i
print("generator:", list(gen()))
print("itertools.cycle:", list(itertools.islice(itertools.cycle([1,2]), 5)))

# --- DICT UNPACKING & FUNCTION CALL UNPACKING ---
d = {'x': 1, 'y': 2}
def foo(x, y): return x + y
print("dict unpacking:", foo(**d))

# --- SET & DICT COMPREHENSIONS ---
set_comp = {x**2 for x in range(5)}
dict_comp = {x: x**2 for x in range(5)}
print("set comp:", set_comp)
print("dict comp:", dict_comp)


# --- TYPEDDICT, LITERAL, PROTOCOL ---
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

# --- CONTEXTLIB: SUPPRESS, REDIRECT_STDOUT ---
with suppress(FileNotFoundError):
    os.remove('no_such_file.txt')
with open('out.txt', 'w') as f, redirect_stdout(f):
    print("redirected to file")
print("redirected file content:", open('out.txt').read())