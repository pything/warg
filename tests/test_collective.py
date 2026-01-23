#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/03/2020
           """

import logging

from warg import evaluate_context, kws_sink, prod, sink

_logger = logging.getLogger(__name__)


def test_a():
    _logger.info(evaluate_context(kws_sink, "str"))
    _logger.info(evaluate_context(kws_sink, 2))
    _logger.info(evaluate_context(kws_sink, 2.2))

    _logger.info(evaluate_context(prod, (2, 2)))

    _logger.info(evaluate_context(prod, (2.2, 2.2)))

    _logger.info(evaluate_context(prod, (2, 2.2)))

    _logger.info(evaluate_context(prod, (2.2, 2)))

    _logger.info(evaluate_context(sink, (2, 2), face=(2.2, 2)))
