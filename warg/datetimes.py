#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 18/03/2020
           """
__all__ = ["default_datetime_repr", "now_repr"]

import datetime
import logging

logger = logging.getLogger(__name__)
DEFAULT_REPRESENTATION = "%Y-%m-%d_%H:%M:%S.%f"


def default_datetime_repr(date: datetime, str_format: str = DEFAULT_REPRESENTATION) -> str:
    """

    :param date:
    :type date:
    :param str_format:
    :type str_format:
    :return:
    :rtype:"""
    return date.strftime(str_format)


def now_repr() -> str:
    """

    :return:
    :rtype:
    """
    return default_datetime_repr(datetime.datetime.now())


if __name__ == "__main__":
    logger.info(now_repr())
