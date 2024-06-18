#!/usr/bin/env python3
__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""
          Plugin

           Created on 13/06/2020
           """

import logging
from typing import Sequence, Tuple

logger = logging.getLogger(__name__)
__all__ = ["split"]


def split(seq: Sequence) -> Tuple[Sequence, Sequence]:
    """

    :param seq:
    :type seq:
    :return:
    :rtype:
    """
    m = len(seq) // 2
    return seq[:m], seq[m:]


if __name__ == "__main__":
    logger.info(split(list(range(11))))
    logger.info(split(list(range(10))))
    logger.info(split(list(range(9))))
