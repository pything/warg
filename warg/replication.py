__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 23/07/2020
           """

__all__ = ["replicate"]

import logging
from typing import Sequence, Union

from warg import Number

_logger = logging.getLogger(__name__)


def replicate(x: Union[Sequence, Number], times: int = 2) -> Sequence:
    """
    if not tuple

    :param times:
    :type times:
    :param x:
    :type x:
    :return:
    :rtype:"""
    if isinstance(x, Sequence):
        if len(x) == times:
            return x
    return (x,) * times


if __name__ == "__main__":

    def asdaa() -> None:
        """
        :rtype: None
        """
        _logger.info(replicate(2))
        _logger.info(replicate(2, 4))

        _logger.info(replicate((2, 3)))
        _logger.info(replicate((2, 3), times=4))

    asdaa()
