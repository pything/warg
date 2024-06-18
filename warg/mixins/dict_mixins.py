#!/usr/bin/env python3


__author__ = "Christian Heider Lindbjerg"
__doc__ = ""

__all__ = [
    "IterDictItemsMixin",
    "IterDictKeysMixin",
    "IterDictValuesMixin",
]

from typing import Any, Tuple
import logging

logger = logging.getLogger(__name__)


class IterDictItemsMixin:
    """
    Mixin class for iterating kw pairs in a class instance __dict__"""

    def __iter__(self) -> Tuple[Any, Any]:
        yield from self.__dict__.items()


class IterDictKeysMixin:
    """
    Mixin class for iterating only the keys of a class instance __dict__"""

    def __iter__(self) -> Any:
        yield from self.__dict__.keys()


class IterDictValuesMixin:
    """
    Mixin class for iterating only the values of a class instance __dict__"""

    def __iter__(self) -> Any:
        yield from self.__dict__.values()


if __name__ == "__main__":

    def asdij() -> None:
        """
        :rtype: None
        """

        class IASD(IterDictValuesMixin):
            pass

        a = IASD()
        a.b = 1
        a.c = 2
        a.d = 3

        for ca in a:
            logger.info(ca)

    asdij()
