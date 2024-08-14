#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

import time
from typing import Tuple


def benchmark_func(func: callable, times: int = 100000) -> Tuple[float, float]:
    """description"""
    start = time.time()
    result = None
    for _ in range(times):
        result = func()
    end = time.time()
    return end - start, result
