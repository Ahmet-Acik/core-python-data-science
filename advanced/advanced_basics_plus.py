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