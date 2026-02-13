__author__ = "Christian Heider Lindbjerg"

import time
from typing import Tuple, Callable


def benchmark_func(func: Callable, times: int = 100000) -> Tuple[float, float]:
    """

    :param func:
    :type func:
    :param times:
    :type times:
    :return:
    :rtype:
    """
    start = time.time()
    result = None
    for _ in range(times):
        result = func()
    end = time.time()
    return end - start, result
