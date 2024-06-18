#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 15-12-2020
           """
import logging

logger = logging.getLogger(__name__)
if __name__ == "__main__":

    def _main():
        from multiprocessing import Pool

        def f(x):
            """description"""
            import config1

            logger.info(config1.A_CONSTANT)
            return x * x

        with Pool(5) as p:
            logger.info(p.map(f, [1, 2, 3]))

    _main()
