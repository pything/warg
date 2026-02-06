__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 11-12-2020
           """
import logging

_logger = logging.getLogger(__name__)
if __name__ == "__main__":

    async def a() -> None:
        """
        :rtype: None
        """
        import addition_config_usage

        await addition_config_usage.b()
        import config2

        _logger.info(config2.ANOTHER_CONSTANT)

    import asyncio

    asyncio.run(a())
