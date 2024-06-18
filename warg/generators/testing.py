#!/usr/bin/env python3
import itertools
from typing import Iterator, Optional

__all__ = ["peek"]

import logging

logger = logging.getLogger(__name__)


def peek(generator: Iterator) -> Optional[itertools.chain]:
    try:
        return itertools.chain((next(generator),), generator)
    except StopIteration:
        return None


if __name__ == "__main__":
    print(peek(iter(range(0))))
    print(peek(iter(range(1))))
