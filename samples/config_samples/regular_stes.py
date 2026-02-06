__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 15-12-2020
           """
import logging

_logger = logging.getLogger(__name__)
if __name__ == "__main__":

    def f() -> None:
        """
        :rtype: None
        """
        import config1

        _logger.info(config1.A_CONSTANT)
        import config1

        _logger.info(config1.ANOTHER_CONSTANT)

    f()
