#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 14/01/2020
           """

__all__ = [
    "kws_sink",
    "sink",
    "prod",
    "collate_first_dim",
    "call_identity",
    "args_sink",
    "identity",
    "invert_shallow_mapping",
    "flip_two_level_mapping",
    "swap_mapping_order",
    "nop",
    "empty_str",
    "list_keys",
    "first_key",
    "last_key",
    "to_list",
    "to_tuple",
    "recurse_replace_empty",
    "text_in_file",
    "int_limits",
    "flatten_mapping",
    "most_common_substrings",
    "mappings_agreement_reduce",
]

import ctypes
import logging
import operator
import sys
import webbrowser
from collections import defaultdict
from copy import deepcopy
from difflib import SequenceMatcher
from functools import reduce
from itertools import product
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple, Union

import requests

from warg.contexts import Suppress
from warg.decorators import drop_unused_kws
from warg.typing_extension import Number

logger = logging.getLogger(__name__)


def int_limits(c_int_type: Any) -> Tuple[int, int]:
    signed = c_int_type(-1).value < c_int_type(0).value
    bit_size = ctypes.sizeof(c_int_type) * 8
    signed_limit = 2 ** (bit_size - 1)
    return (-signed_limit, signed_limit - 1) if signed else (0, 2 * signed_limit - 1)


TO_LIST_MAX_RECURSION_LIMIT = int_limits(ctypes.c_int)[-1]


def recurse_replace_empty(iterable: Iterable) -> Optional[Iterable]:
    if isinstance(iterable, str) or not isinstance(iterable, Iterable):
        return iterable

    if iterable:
        if isinstance(iterable, Mapping):
            return {k: recurse_replace_empty(v) for k, v in iterable.items()}

        # noinspection PyArgumentList
        return type(iterable)(
            recurse_replace_empty(i) for i in iterable
        )  # contstruct type of iterable with replaced empties

    return None


def list_keys(d: Dict) -> List[Any]:
    return list(d.keys())


def first_key(d: Dict) -> Any:
    return list_keys(d)[0]


def last_key(d: Dict) -> Any:
    return list_keys(d)[-1]


def empty_str() -> str:
    """

    :return:
    :rtype:
    """
    return ""


def nop() -> None:
    """
    :rtype: None
    """
    pass


def identity(a: Any) -> Any:
    """description"""
    return a


@drop_unused_kws
def kws_sink(*args) -> Tuple[Any, ...]:
    """
    Returns args without any modification what so ever. Drops kws
    :return:"""
    return args


def call_identity(*args, **kwargs) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
    """

    :param args:
    :param kwargs:
    :return:"""
    return args, kwargs


# noinspection PyUnusedLocal
def args_sink(*args, **kwargs) -> Dict[str, Any]:
    """

    :param args:
    :param kwargs:
    :return:"""
    return kwargs


# noinspection PyUnusedLocal
def sink(*args, **kwargs) -> None:
    """
    Returns None, but accepts everything

    :param args:
    :param kwargs:
    :return:"""
    return


def prod(iterable: Iterable[Number]) -> Number:
    """
    Calculate the product of an Iterable, of int or floats
    :param iterable:
    :return:"""
    return reduce(operator.mul, iterable, 1)


def collate_first_dim(batch: Iterable) -> Tuple:
    """

    :param batch:
    :return:"""
    return tuple(zip(*batch))


def invert_shallow_mapping(m: Mapping) -> Dict:
    """

    :param m:
    :return:
    """
    return {v: k for k, v in m.items()}


def flip_two_level_mapping(m: Mapping) -> Dict:
    """
    result = {}
    [result.setdefault(a, {}).update({k:b}) for k, v in m.items() for a, b in v.items()]
    return result

    :param m:
    :return:
    """

    flipped = defaultdict(dict)
    for key, val in m.items():
        for sub_key, sub_val in val.items():
            flipped[sub_key][key] = sub_val
    return flipped


def swap_mapping_order(m: Mapping, order: Sequence[int]) -> Mapping:
    """

    :param m:
    :param order:
    :return:
    """
    order = [*order]

    def deep_swap(dict_, level):
        """

        :param dict_:
        :param level:
        :return:
        """

        def swap_two_level_dict(a):
            """

            :param a:
            :return:
            """
            b = defaultdict(dict)
            for key1, value1 in a.items():
                for key2, value2 in value1.items():
                    b[key2].update({key1: value2})
            return b

        dict_ = deepcopy(dict_)
        if level == 0:
            dict_ = swap_two_level_dict(dict_)
        else:
            for key in dict_:
                dict_[key] = deep_swap(dict_[key], level - 1)
        return dict_

    for pas_no in range(len(order) - 1, 0, -1):
        for i in range(pas_no):
            if order[i] > order[i + 1]:
                temp = order[i]
                order[i] = order[i + 1]
                order[i + 1] = temp
                m = deep_swap(m, i)
    return m


def chain_filter(it: Iterable, *filters: Callable) -> Iterator:
    """
    Apply a sequence of callables to an iterable through filter; filtering the iterable to the subset of a callable
    returns

    Args:
        it (Iterable):
            iterable to be filtered
        filters (Callable):
            The filter callables

    Returns:
        Iterator:
            returns an iterator yielding those items of iterable for which all(filters(item)) is true. If filters are
            None, return the items that are true.
    """
    for f in filters:
        it = filter(f, it)
    return it


def chain_apply(it: Iterable, *callables: Callable) -> Iterable[Any]:
    """
    Apply a sequence of callables to an iterable; apply the iterable sequentially in callables order

    Args:
        it (Iterable):
            iterable to be applied to
        callables (Callable):
             The applying callables

    Returns:
        Iterable:
            returns the iterable with all the callables applied.
    """
    for f in callables:
        it = f(it)
    return it


def to_list(x: Union[Iterable, Any]) -> Union[List, Any]:
    if False:
        if x is None:
            return []

    if TO_LIST_MAX_RECURSION_LIMIT:
        original = sys.getrecursionlimit()
        sys.setrecursionlimit(TO_LIST_MAX_RECURSION_LIMIT)

    if not isinstance(x, Iterable):
        return x

    i = iter(x)

    try:
        val = next(i)
    except StopIteration:
        return []
    finally:
        if TO_LIST_MAX_RECURSION_LIMIT:
            sys.setrecursionlimit(original)

    return [to_list(val)] + to_list(i)


def to_tuple(x: Union[Iterable, Any]) -> Union[Tuple, Any]:
    if False:
        if x is None:
            return ()

    if TO_LIST_MAX_RECURSION_LIMIT:
        original = sys.getrecursionlimit()
        sys.setrecursionlimit(TO_LIST_MAX_RECURSION_LIMIT)

    if not isinstance(x, Iterable):
        return x

    i = iter(x)

    try:
        val = next(i)
    except StopIteration:
        return ()
    finally:
        if TO_LIST_MAX_RECURSION_LIMIT:
            sys.setrecursionlimit(original)

    return (to_tuple(val), *to_tuple(i))


@Suppress(FileNotFoundError)
def text_in_file(text: str, filename: Path) -> bool:
    if filename.exists():
        return any(text in line for line in filename.open())

    return False


def flatten_mapping(mapping: Mapping[str, Any], seperator: str = "_") -> Mapping[str, Any]:
    """
    iterates and recursively flattens nested mappings by appending keys for each level


    :param seperator:
    :param mapping: nested mapping to flatten
    :return: a single level mapping with appended level keys
    """
    out_dict = {}
    for k, v in mapping.items():
        if isinstance(v, Mapping):
            out_dict.update(**{f"{k}{seperator}{ki}": vi for ki, vi in flatten_mapping(v, seperator).items()})
        else:
            out_dict[k] = v

    return out_dict


def most_common_substrings(
    strings: Iterable[str], min_common_substring: int = 2, min_common_count: int = 2
) -> List[str]:
    """
    Finds common substrings in Iterable of strings, ordered in most to least occurring

    :param strings:
    :param min_common_substring:
    :param min_common_count:
    :return:
    """
    name_matches = []

    for z1, z2 in product(strings, strings):
        if z1 != z2:
            match = SequenceMatcher(isjunk=None, a=z1, b=z2).find_longest_match(
                alo=0, ahi=len(z1), blo=0, bhi=len(z2)
            )
            match_string = z1[match.a : match.a + match.size]
            if len(match_string) >= min_common_substring:
                name_matches.append(match_string)

    return sorted({i for i in name_matches if name_matches.count(i) >= min_common_count})


def mappings_agreement_reduce(m1: Mapping[Any, Any], m2: Mapping[Any, Any]) -> Mapping[Any, Any]:
    """
    takes two mappings and reduces it to one mapping, if the agree or one of them is None take one or the other. if
    they disagree the resulting value is None.

    :param m1: A mapping
    :param m2: Another mapping
    :return: a single mapping
    """
    out = {}
    for k, v in m1.items():
        if k not in m2 or v == m2[k] or not m2[k]:
            out[k] = v
        elif not v and k in m2:
            out[k] = m2[k]
        else:
            out[k] = None

    for k, v in m2.items():
        if k not in out:
            out[k] = v

    return out


def open_uri_resource(uri: str) -> str:
    """Opens the default web browser.
    Qt offers PyQt5.QtWebEngineWidgets (QWebEngineView, QWebEngineSettings) but they are not
    available from pyQGIS

    """

    path = Path(uri)

    if path.exists() and path.is_file():
        uri = f"file:///{path.absolute()}"
        msg = uri
        webbrowser.open_new_tab(uri)
    else:
        try:
            uri = f'https://{uri.replace("https://","")}'
            r = requests.head(uri)
            if r.ok:  # it is a boolean
                try:
                    webbrowser.open_new_tab(uri)
                    msg = uri
                except webbrowser.Error as e:
                    msg = f"Webbrowser error: {e}"

            elif r.status_code == 404:
                msg = f'HTTP Error 404: Page not found.<br>The following URL may be broken or dead:<br><br><a href="{uri}">{uri}</a>'

            else:
                msg = f'Error with URL<br><br><a href="{uri}">{uri}</a>'

        except requests.ConnectionError as e:
            msg = f'URL <a href="{uri}">{uri}</a> could not be opened.<br><br>Is your internet connection up and working?'

    return msg


if __name__ == "__main__":

    def asud() -> None:
        """
        :rtype: None
        """
        a = {"b": 1, "h": 2}
        logger.info(invert_shallow_mapping(a))

    def asjdnasid() -> None:
        """
        :rtype: None
        """
        a = {
            "b": {"c": {"d": [0, 1, 2], "e": [3, 4, 5, 6]}, "f": [7, 8], "g": [9]},
            "h": {"j": [10, 11]},
        }
        logger.info(flip_two_level_mapping(a))

    def asidj() -> None:
        """
        :rtype: None
        """
        test_dict = {
            "a": {"c": {"e": 0, "f": 1}, "d": {"e": 2, "f": 3}},
            "b": {"c": {"g": 4, "h": 5}, "d": {"j": 6, "k": 7}},
        }
        result = swap_mapping_order(test_dict, [2, 0, 1])
        logger.info(result)

    def i8jsadij():
        ij = ([10, 29], [(2, 3, 4), [[12, 4, 5]], ((2, 92, 90))], [])
        logger.info(to_list(ij))

    def i8jsadi2j():
        ij = ([10, 29], [(2, 3, 4), [[12, 4, 5]], ((2, 92, 90))], [])
        logger.info(to_tuple(ij))

    # i8jsadij()
    # i8jsadi2j()
    # asud()
    # asidj()
    # asjdnasid()

    # logger.info(open_uri_resource(__file__))
    logger.info(open_uri_resource("dr.dk"))
