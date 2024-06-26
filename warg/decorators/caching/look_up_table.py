#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""
          Automatically generates a look up data

           Created on 06/03/2020
           """

import logging
from time import sleep, time
from typing import Any, Callable, Iterable, Mapping, MutableMapping, Sequence, Set, Tuple

from warg.decorators.hashing import make_hash

logger = logging.getLogger(__name__)
global_table = {}

__all__ = ["add_lut", "look_up", "look_up_args", "look_up_kws"]


def add_lut(f: Callable) -> callable:
    """

    :param f:
    :type f:
    :return:
    :rtype:"""
    global_table[f] = {}
    return f


def look_up(f: Callable, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]) -> Any:
    """

    :param f:
    :type f:
    :param args:
    :type args:
    :param kwargs:
    :type kwargs:
    :return:
    :rtype:"""
    ag_hash = hash(args) + make_hash(kwargs)
    if f in global_table:
        if ag_hash in global_table[f]:
            return global_table[f][ag_hash]

        res = global_table[f][ag_hash] = f(*args, **kwargs)
        return res

    global_table[f] = {}
    res = global_table[f][ag_hash] = f(*args, **kwargs)
    return res


def look_up_args(f: Callable, *args: Sequence) -> Any:
    """

    :param f:
    :type f:
    :param args:
    :type args:
    :return:
    :rtype:"""
    if f in global_table:
        if args in global_table[f]:
            return global_table[f][args]

        res = global_table[f][args] = f(*args)
        return res

    global_table[f] = {}
    res = global_table[f][args] = f(*args)
    return res


def look_up_kws(f: Callable, **kwargs: MutableMapping) -> Any:
    """

    :param f:
    :type f:
    :param kws:
    :type kws:
    :return:
    :rtype:"""
    kw_hash = make_hash(kwargs)
    if f in global_table:
        if kw_hash in global_table[f]:
            return global_table[f][kw_hash]

        res = global_table[f][kw_hash] = f(**kwargs)
        return res

    global_table[f] = {}
    res = global_table[f][kw_hash] = f(**kwargs)
    return res


def precompute_lut(f: Callable, arg_sets: Set[Tuple[Iterable, Mapping]], *, verbose=False) -> callable:
    """

    :param f:
    :type f:
    :param arg_sets:
    :type arg_sets:
    :param verbose:
    :type verbose:
    :return:
    :rtype:"""
    for arg_set, kws_set in arg_sets:
        res = look_up(f, *arg_set, **kws_set)
        if verbose:
            logger.info(f"precompute {f},{arg_set},{kws_set}->{res}")
    return f


def precompute_lut_args(f: Callable, arg_sets: Set[Iterable], *, verbose=False) -> callable:
    """

    :param f:
    :type f:
    :param arg_sets:
    :type arg_sets:
    :param verbose:
    :type verbose:
    :return:
    :rtype:"""
    for arg_set in arg_sets:
        res = look_up_args(f, *arg_set)
        if verbose:
            logger.info(f"precompute {f},{arg_sets}->{res}")
    return f


def precompute_lut_kws(f: Callable, arg_sets: Set[Mapping], *, verbose=False) -> callable:
    """

    :param f:
    :type f:
    :param arg_sets:
    :type arg_sets:
    :param verbose:
    :type verbose:
    :return:
    :rtype:"""
    for arg_set in arg_sets:
        res = look_up_kws(f, **arg_set)
        if verbose:
            logger.info(f"precompute {f},{arg_sets}->{res}")
    return f


def precompute_lut_dec(arg_sets, *, verbose=False):
    """

    :param arg_sets:
    :type arg_sets:
    :param verbose:
    :type verbose:
    :return:
    :rtype:"""

    def rdec(f):
        """

        :param f:
        :type f:
        :return:
        :rtype:"""
        precompute_lut(f, arg_sets, verbose=verbose)
        return f

    return rdec


def precompute_lut_args_dec(arg_sets, *, verbose: bool = False):
    """

    :param arg_sets:
    :type arg_sets:
    :param verbose:
    :type verbose:
    :return:
    :rtype:"""

    def rdec(f):
        """

        :param f:
        :type f:
        :return:
        :rtype:"""
        precompute_lut_args(f, arg_sets, verbose=verbose)
        return f

    return rdec


if __name__ == "__main__":

    @add_lut
    def my_function(foo, bar):
        """

        :param foo:
        :type foo:
        :param bar:
        :type bar:
        :return:
        :rtype:"""
        return foo + bar

    result = look_up_args(my_function, 0, 8)
    logger.info(result)
    result = look_up_args(my_function, 8, 0)
    logger.info(result)

    @precompute_lut_args_dec(list(zip(range(9), list(range(9))[::-1])))
    def my_function2(foo, bar):
        """

        :param foo:
        :type foo:
        :param bar:
        :type bar:
        :return:
        :rtype:"""
        sleep(0.1)
        return bar * foo

    a = time()
    look_up_args(my_function2, 0, 8)
    logger.info(time() - a)
    a = time()
    look_up_args(my_function2, 8, 0)
    logger.info(time() - a)

    result = look_up(my_function2, 14, bar=21)
    logger.info(result)

    result = look_up(my_function2, 14, bar=21)
    logger.info(result)

    result = look_up(my_function2, 104, bar=2)
    logger.info(result)

    result = look_up_args(my_function, 1, 2)
    logger.info(result)

    result = look_up_args(my_function, 1, 2)
    logger.info(result)

    result = look_up_args(my_function, 12, 2)
    logger.info(result)

    result = look_up_args(my_function2, 1, 2)
    logger.info(result)

    result = look_up_kws(my_function2, foo=1, bar=2)
    logger.info(result)
