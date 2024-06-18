#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

__doc__ = """description"""
__all__ = ["to_british_english", "deamericanise"]

import logging
from types import MappingProxyType
from typing import Mapping

logger = logging.getLogger(__name__)
default_rules = MappingProxyType(
    {
        "ize": "ise",
        "yze": "yse",
        "iza": "isa",
        "aluminum": "aluminium",
        # 'se': 'ce',
        # 'og': 'ogue',
    }
)


def to_british_english(text: str, rules: Mapping = default_rules) -> str:
    """

    :param text:
    :type text: str
    :param rules:
    :type rules: Mapping
    :return: text
    :rtype: str
    """
    for r in rules.items():
        text = text.replace(*r)

    return text


def deamericanise(text: str) -> str:
    """
    Naively exchanges 'z' in english texts

    convert to 'British English'

    :param text: some text
    :type text: str
    :return: deamericanised text
    :rtype: str
    """
    return to_british_english(text)


if __name__ == "__main__":
    logger.info(
        deamericanise(
            "I analyzed websites in order to recognize the correct spelling of international organizations"
        )
    )
