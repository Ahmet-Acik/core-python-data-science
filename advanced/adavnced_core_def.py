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