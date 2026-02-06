__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 28-01-2021
           """

import logging

from warg import kws_sink, prod, sink

_logger = logging.getLogger(__name__)


def test_a():
    _logger.info(kws_sink("str"))
    _logger.info(kws_sink(2))
    _logger.info(kws_sink(2.2))

    _logger.info(prod((2, 2)))

    _logger.info(prod((2.2, 2.2)))

    _logger.info(prod((2, 2.2)))

    _logger.info(prod((2.2, 2)))

    _logger.info(sink((2, 2), face=(2.2, 2)))
