__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 15-12-2020
           """
import logging

_logger = logging.getLogger(__name__)
if __name__ == "__main__":

    def _main():
        from multiprocessing import Pool

        def f(x):
            """description"""
            import config1

            _logger.info(config1.A_CONSTANT)
            return x * x

        with Pool(5) as p:
            _logger.info(p.map(f, [1, 2, 3]))

    _main()
