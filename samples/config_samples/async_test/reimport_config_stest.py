#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 11-12-2020
           """
import logging

logger = logging.getLogger(__name__)
if __name__ == "__main__":

    async def a() -> None:
        """
        :rtype: None
        """
        import addition_config_usage

        await addition_config_usage.b()
        import config2

        logger.info(config2.ANOTHER_CONSTANT)

    import asyncio

    asyncio.run(a())
