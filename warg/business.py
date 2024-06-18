#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 17/03/2020
           """

import logging
from itertools import cycle
from typing import Callable, Iterable

logger = logging.getLogger(__name__)


def busy_indicator(
    *,
    stream: Callable = print,
    indicator_interval: int = 1,
    phases: Iterable[str] = ("◑", "◒", "◐", "◓"),
) -> Iterable[int]:
    """
    You can choose arbitrary phases like ['|','/','-','\\']

    :param stream:
    :type stream:
    :param indicator_interval:
    :type indicator_interval:
    :param phases:
    :type phases:
    :return:
    :rtype:"""

    phases = cycle(phases)
    i = 0
    while True:
        if i % indicator_interval == 0:
            stream(f"{next(phases)}", end="\r", flush=True)
        yield i
        i += 1


if __name__ == "__main__":

    def main() -> None:
        """description"""
        import time

        for i in busy_indicator(indicator_interval=10):
            time.sleep(0.1)
            if i > 100:
                break

    main()
