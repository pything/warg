#!/usr/bin/env python3
import copy
import logging
from typing import Any

logger = logging.getLogger(__name__)
DictProxyType = type(object.__dict__)

__all__ = ["make_hash"]


def make_hash(o: Any) -> int:
    """
    Makes a hash from a dictionary, list, tuple or set to any level, that
    contains only other hashable types (including any lists, tuples, sets, and
    dictionaries). In the case where other kinds of objects (like classes) need
    to be hashed, pass in a collection of object attributes that are pertinent.
    For example, a class can be hashed in this fashion:

      make_hash([cls.__dict__, cls.__name__])

    A function can be hashed like so:

      make_hash([fn.__dict__, fn.__code__])"""

    if isinstance(o, DictProxyType):
        o2 = {}
        for k, v in o.items():
            if not k.startswith("__"):
                o2[k] = v
        o = o2

    if isinstance(o, (set, tuple, list)):
        return hash(tuple([make_hash(e) for e in o]))
    if not isinstance(o, dict):
        return hash(o)

    new_o = copy.deepcopy(o)
    for k, v in new_o.items():
        new_o[k] = make_hash(v)

    return hash(tuple(frozenset(sorted(new_o.items()))))


if __name__ == "__main__":
    logger.info(hash(1))
    logger.info(make_hash(1))
    logger.info(make_hash(1))
    logger.info(make_hash({1}))
    logger.info(make_hash([1]))
    logger.info(make_hash({1}))
    logger.info(make_hash({1, 2}))
    logger.info(make_hash([1, 2]))
    logger.info(make_hash((1, 2)))
    logger.info(make_hash({4}))
    logger.info(make_hash("1"))
    logger.info(make_hash({"2": 2}))
    logger.info(make_hash({"2": 3}))
    logger.info(make_hash({"3": 2}))
    logger.info(make_hash({"3": 3}))
