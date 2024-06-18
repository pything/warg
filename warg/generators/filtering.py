#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 18-01-2021
           """

import logging
from enum import Enum
from typing import Any, Iterable

logger = logging.getLogger(__name__)
__all__ = ["FilterModeEnum", "symbol_filter"]


# from sorcery import assigned_names # PURE!


class FilterModeEnum(Enum):
    """
    Filter Mode
    """

    # exclude_postfix, exclude_prefix, exclude_fully = assigned_names()
    # TODO: Include variants
    exclude_postfix, exclude_prefix, exclude_fully = (
        "exclude_postfix",
        "exclude_prefix",
        "exclude_fully",
    )


def symbol_filter(
    string_stream: Iterable[str],
    symbol: str = "#",
    *,
    exclusion_mode: FilterModeEnum = FilterModeEnum.exclude_postfix,
) -> Any:
    """description"""
    if exclusion_mode == FilterModeEnum.exclude_fully:
        yield from filter(lambda s: symbol not in s, string_stream)
    elif exclusion_mode == FilterModeEnum.exclude_postfix or exclusion_mode == FilterModeEnum.exclude_prefix:
        selector = 0
        if exclusion_mode == FilterModeEnum.exclude_prefix:
            selector = -1
        for s in string_stream:
            raw = s.split(symbol)[selector].strip()
            if raw:
                yield raw
    else:
        raise NotImplemented(f"{exclusion_mode} mode not supported")


if __name__ == "__main__":

    def asijsda() -> None:
        """
        :rtype: None
        """
        strings = [
            " # aasd # sad ",
            " faojasasd # oiwaos ",
            " okjasifj  oajsidw2 ",
            " 12 329#9213",
        ]
        for s in symbol_filter(strings):
            logger.info(s)

        logger.info(" ")

        for i, s in enumerate(symbol_filter(strings, exclusion_mode=FilterModeEnum.exclude_fully)):
            logger.info(i, s)

        logger.info(" ")

        for s in symbol_filter(strings, exclusion_mode=FilterModeEnum.exclude_prefix):
            logger.info(s)

    asijsda()
