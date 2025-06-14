#!/usr/bin/env python3
import logging
from typing import Callable, Dict, Hashable, Iterable, Mapping, MutableMapping
from collections import defaultdict


logger = logging.getLogger(__name__)
__all__ = [
    "invert_mapping",
    "invert_dict",
    "AppendingDict",
    "pivot_dict_object",
    "pivot_dict",
    "to_dict",
    "nested_dict",
]


def append_to_dict(d: Dict, key, value) -> Dict:
    """

    :param d:
    :type d:
    :param key:
    :type key:
    :param value:
    :type value:
    :return:
    :rtype:
    """
    d.setdefault(key, []).append(value)
    return d


class AppendingDict(Dict):  # appending_dict = collections.defaultdict(list)
    def __setitem__(self, key, value):
        # self.setdefault(key, []).append(value)
        # append_to_dict(self, key, value)
        if key in self:
            self[key].append(value)
        else:
            super().__setitem__(key, [value])


def recurse_mapping(a: Mapping, call: Callable = print) -> None:
    for k, v in a.items():
        if isinstance(v, Mapping):
            recurse_mapping(v)
        call(v)


def invert_mapping(m: Mapping) -> Mapping:  # TODO: TEST THIS; MAY CONTAINS BUGS!
    """
    Invert a mapping

    if a mapping does not have duplicate hashable values, then this is the same as invert_dict, otherwise values in
    new_m are tuples of keys with duplicate values
    :return: :rtype:
    """

    if isinstance(m, MutableMapping):
        new_m = type(m)()
    else:
        new_m = {}

    for k, v in m.items():
        if not isinstance(v, Hashable):
            raise TypeError(f"values must be hashable, was {type(v), v}, for key {k}")
        if v in new_m:
            if isinstance(new_m[v], Iterable) and (not isinstance(new_m[v], str)):
                new_m[v] = (*new_m[v], k)
            else:
                new_m[v] = [new_m[v], k]
        else:
            new_m[v] = k
    return new_m


def invert_dict(d: Mapping) -> Dict:  # TODO: HANDLE DUPLICATE KEYS; CONVERT TO TUPLES
    """
    Invert a dict

    :param d:
    :type d:
    :return:
    :rtype:
    """
    return {v: k for k, v in d.items()}


def pivot_dict(d: Dict, key) -> Dict:  # TODO: HANDLE DUPLICATE KEYS; CONVERT TO TUPLES
    """
    pivot_key -> pivot_value

    :param d:
    :param key:
    :return:
    :rtype:
    """
    return {v[key]: k for k, v in d.items()}


def pivot_dict_object(d: Dict, key) -> Dict:  # TODO: HANDLE DUPLICATE KEYS; CONVERT TO TUPLES
    """
    pivot_key -> pivot_value for object attributes

    :param d:
    :param key:
    :return:
    :rtype:
    """
    return {getattr(v, key): k for k, v in d.items()}


def to_dict(m: Mapping) -> dict:
    o = {}
    for k, v in m.items():
        if isinstance(v, Mapping):
            o[k] = to_dict(v)
        elif isinstance(v, str):
            o[k] = v
        elif isinstance(v, Iterable):
            o[k] = [to_dict(v_) if isinstance(v_, Mapping) else v_ for v_ in v]
        else:
            o[k] = v
    return o


nested_dict = lambda: defaultdict(nested_dict)

if __name__ == "__main__":
    logger.info(invert_mapping({"a": 1, "b": 2}))

    logger.info(invert_mapping({"a": 2, "b": 2, "c": 3, "d": 4}))
    logger.info(invert_dict({"a": 2, "b": 2, "c": 3, "d": 4}))

    def uhasdu():
        from warg.data_structures.named_ordered_dictionary import NOD

        a = NOD({"b": NOD(c=1)}, d="usahfo7uyhaouw", f=[NOD(p="m")])

        logger.info(a)
        logger.info(a.as_dict())

    uhasdu()

    # logger.info(pivot_dict_object({"a": 2, "b": 2, "c": 3, "d": 4}, "id"))
