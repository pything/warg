#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 11/12/2019
           """

__all__ = ["PostInit"]

import logging
from typing import Any, MutableMapping, Sequence

logger = logging.getLogger(__name__)


class PostInit(type):
    """
    define a new metaclass which overrides the "__call__" function"""

    def __call__(cls, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]) -> object:
        """
        Called when you call a class type constructor()"""
        obj = type.__call__(cls, *args, **kwargs)
        if hasattr(obj, "__post_init__"):
            obj.__post_init__(*args, **kwargs)
        return obj


if __name__ == "__main__":

    class SAD(metaclass=PostInit):
        """description"""

        def __init__(self):
            logger.info("init")

        def __post_init__(self) -> None:
            """description"""
            logger.info("post_init")

    SAD()
    SAD()
