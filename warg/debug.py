#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/03/2020
           """

__all__ = ["evaluate_context"]

import logging
from typing import Any, Callable, Dict, List, MutableMapping, Tuple

logger = logging.getLogger(__name__)


def evaluate_context(
    x: Any, *args: Any, **kwargs: MutableMapping[str, Any]
) -> Tuple[List, Dict, object, type]:
    """

    :rtype: Tuple[List,Dict,object,type]
    :param x:
    :param args:
    :param kwargs:
    :return:"""
    if isinstance(x, Callable):
        x = x(*args, **kwargs)
    return (
        [evaluate_context(a) for a in args],
        {k: evaluate_context(v) for k, v in kwargs.items()},
        x,
        type(x),
    )


if __name__ == "__main__":
    logger.info(evaluate_context(print, 2, 2))
