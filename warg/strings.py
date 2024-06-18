#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/10/2019
           """

__all__ = ["indent_lines", "str_to_tuple", "clean_string"]

import logging
from typing import Any

logger = logging.getLogger(__name__)


def indent_lines(input_str: Any, indent_spaces_num: int = 2, ignore_single_lines: bool = False) -> str:
    """

    :param ignore_single_lines:
    :type ignore_single_lines:
    :param input_str:
    :type input_str:
    :param indent_spaces_num:
    :type indent_spaces_num:
    :return:
    :rtype:"""
    if not isinstance(input_str, str):
        input_str = str(input_str)
    s = input_str.split("\n")
    indent_s = indent_spaces_num * " "
    if len(s) == 1:
        if ignore_single_lines:
            return input_str
        else:
            return f"{indent_s}{input_str}"
    first = s.pop(0)
    s = [f"{indent_s}{line}" for line in s]
    s = "\n".join(s)
    s = f"{indent_s}{first}\n{s}"
    return s


def str_to_tuple(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    return tuple(map(int, arg.split()))


def clean_string(s: str) -> str:
    return s.lower().strip().replace(" ", "_")


if __name__ == "__main__":
    a = "slasc\nsaffasd\n2dasf"
    logger.info(a)
    logger.info(indent_lines(a))
