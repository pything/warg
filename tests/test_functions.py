#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 28-01-2021
           """

from warg import kws_sink, prod, sink

import logging

logger = logging.getLogger(__name__)


def test_a():
    logger.info(kws_sink("str"))
    logger.info(kws_sink(2))
    logger.info(kws_sink(2.2))

    logger.info(prod((2, 2)))

    logger.info(prod((2.2, 2.2)))

    logger.info(prod((2, 2.2)))

    logger.info(prod((2.2, 2)))

    logger.info(sink((2, 2), face=(2.2, 2)))
