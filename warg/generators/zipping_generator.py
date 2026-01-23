#!/usr/bin/env python3
from copy import deepcopy
from typing import Any, Generator, Iterable, Iterator

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 28/10/2019
           """

__all__ = ["unzip", "unzipper"]

import logging

_logger = logging.getLogger(__name__)


def unzip(iterable: Iterable[Any]) -> Iterable[Any]:
    """description"""
    return zip(*iterable)


def unzipper(_iterable: Iterable[Iterable[Any]]) -> Iterable[Any]:
    """
    Unzips an iterable of an iterable

    Be careful, functionality maybe have undefined and unexpected behaviour

    :param _iterable:
    :return:Iterable
    """

    def check_next_iter(iterable_: Any) -> Any:
        """description"""
        if isinstance(iterable_, Iterable):
            try:
                a_ = next(iter(iterable_))
                if isinstance(a_, Iterable):
                    return a_
            except StopIteration:
                pass

    if isinstance(_iterable, Iterable):
        check_a = check_next_iter(check_next_iter(deepcopy(_iterable)))
        if check_next_iter(check_a):
            for a in _iterable:
                yield unzipper(a)
        elif check_a:
            for a in _iterable:
                yield unzip(a)
        else:
            yield from _iterable


if __name__ == "__main__":

    def recursive_eval(node: Any):
        """description"""
        if isinstance(node, (Iterable, Generator, Iterator)):
            gather = []
            for i in node:
                gather.append(recursive_eval(i))
            return gather
        return node

    def aasda() -> None:
        """
        :rtype: None
        """
        r = range(4)

        _logger.info(0)

        a = [[[*r] for _ in r] for _ in r]
        _logger.info(a)

        _logger.info(1)

        for _, assd in zip(r, unzipper(a)):
            _logger.info()
            _logger.info(recursive_eval(assd))
            _logger.info()

        for _, (a, *_) in zip(r, unzipper(a)):
            _logger.info()
            _logger.info(recursive_eval(a))
            _logger.info()

        _logger.info(2)

    def skad23() -> None:
        """
        :rtype: None
        """
        _logger.info(0)
        zippy_once = zip(range(6), range(3))
        dsadsa = list(deepcopy(zippy_once))
        zippy_twice = zip(dsadsa, dsadsa)
        zippy_twice_copy = deepcopy(zippy_twice)
        asds = list(deepcopy(zippy_twice_copy))
        zippy_trice = zip(asds, asds)
        zippy_trice_copy = deepcopy(zippy_trice)

        _logger.info(1)

        for aa in zippy_twice:
            _logger.info(recursive_eval(aa))

        _logger.info(2)

        for a1 in unzip(zippy_twice_copy):
            _logger.info(recursive_eval(a1))

        _logger.info(3)

        for a1 in unzip(zippy_once):
            _logger.info(recursive_eval(a1))

        _logger.info(4)

        for a1 in zippy_trice:
            _logger.info(recursive_eval(a1))

        _logger.info(5)

        for a1 in unzip(zippy_trice_copy):
            _logger.info(recursive_eval(a1))

        _logger.info(6)

    def skad() -> None:
        """
        :rtype: None
        """
        _logger.info(0)
        zippy_once = zip(zip(range(6), range(3)))
        zippy_once_copy = deepcopy(zippy_once)
        dsadsa = list(deepcopy(zippy_once))
        zippy_twice = zip(dsadsa, dsadsa)
        zippy_twice_copy = deepcopy(zippy_twice)
        asds = list(deepcopy(zippy_twice_copy))
        zippy_trice = zip(asds, asds)
        zippy_trice_copy = deepcopy(zippy_trice)
        asds2323 = list(deepcopy(zippy_trice_copy))
        zippy_quad = zip(asds2323, asds2323)
        zippy_quad_copy = deepcopy(zippy_quad)

        _logger.info(1)

        for aa in zippy_twice:
            _logger.info(recursive_eval(aa))

        _logger.info(2)

        for a1 in unzipper(zippy_twice_copy):
            _logger.info(recursive_eval(a1))

        _logger.info(3)

        for a1 in zippy_once_copy:
            _logger.info(recursive_eval(a1))

        _logger.info(4)

        for a1 in unzipper(zippy_once):
            _logger.info(recursive_eval(a1))

        _logger.info(5)

        for a1 in zippy_trice:
            _logger.info(recursive_eval(a1))

        _logger.info(6)

        for a1 in unzipper(zippy_trice_copy):
            _logger.info(recursive_eval(a1))

        _logger.info(7)

        for a1 in zippy_quad:
            _logger.info(recursive_eval(a1))

        _logger.info(8)

        for a1 in unzipper(zippy_quad_copy):
            _logger.info(recursive_eval(a1))

        _logger.info(9)

    aasda()

    _logger.info()
    _logger.info("asafasdw")
    _logger.info()

    skad()
    # skad23()
