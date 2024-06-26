#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 28-01-2021
           """

from warg import get_first_arg_name, identity


import logging

logger = logging.getLogger(__name__)


def test_ausdh3():
    from typing import Any

    def some_func(a: Any) -> None:
        """description"""
        logger.info(get_first_arg_name("some_func", verbose=True))

    some_func(logger.info(2, sep="-"))


def test_ausd2h3():
    from typing import Any

    def some_func(a: Any) -> None:
        """description"""
        logger.info(get_first_arg_name("some_func", verbose=True))

    some_func(identity(2))


def test_ausd2h34():
    from typing import Any

    def some_func(a: Any) -> None:
        """description"""
        logger.info(get_first_arg_name("some_func", verbose=True))

    asd = 2
    some_func(identity(asd))


def test_ausd2h3213():
    from typing import Any

    class Ac:
        class Bc:
            @staticmethod
            def c(d):
                """description"""
                pass

    def some_func(a: Any) -> None:
        """description"""
        logger.info(get_first_arg_name("some_func", verbose=True))

    some_func(Ac.Bc.c(2))


if __name__ == "__main__":
    test_ausdh3()
    test_ausd2h3()
    test_ausd2h3213()
