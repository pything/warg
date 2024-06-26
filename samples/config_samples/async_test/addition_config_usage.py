#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 11-12-2020
           """
import logging

logger = logging.getLogger(__name__)


async def b() -> None:
    """
    :rtype: None
    """
    import config2

    logger.info(config2.A_CONSTANT)


if __name__ == "__main__":

    async def c() -> None:
        """
        :rtype: None
        """
        await b()

    import asyncio

    asyncio.run(c())
