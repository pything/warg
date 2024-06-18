#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 23/07/2020
           """

__all__ = ["recursive_flatten"]


import logging
from typing import Iterable, Sequence

logger = logging.getLogger(__name__)


def recursive_flatten_seq(seq: Sequence) -> Sequence:
    """Depth first flatten"""
    if not seq:  # is empty Sequence
        return seq
    if isinstance(seq[0], Sequence):
        return (*recursive_flatten(seq[0]), *recursive_flatten(seq[1:]))
    return (*seq[:1], *recursive_flatten(seq[1:]))


def recursive_flatten(sequence: Iterable) -> Iterable:
    """
    Depth first flattens iterable

    >>> list(recursive_flatten([1, [2], 3]))
    [1, 2, 3]
    >>> list(recursive_flatten([1, [2], [3, [4]]]))
    [1, 2, 3, 4]
    >>> list(recursive_flatten((([[None]], 2), (2,), 2)))
    [None, 2, 2, 2]
    """
    for element in sequence:
        if isinstance(element, Iterable) and not isinstance(element, str):
            yield from recursive_flatten(element)
        else:
            yield element


if __name__ == "__main__":
    logger.info(list(recursive_flatten((((2,), 2), (2,), 2))))
    logger.info(list(recursive_flatten(((("2",), 2), (2,), 2))))
    logger.info(list(recursive_flatten((([[None]], 2), (2,), 2))))

    logger.info(list(recursive_flatten((([[None]], 2), (2,), 2))))
