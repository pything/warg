#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 02/03/2020
           """

__all__ = ["NoData", "IncompatiblePackageVersions"]

import logging
import types
from typing import Iterable, Union

logger = logging.getLogger(__name__)


class NoData(Exception):
    """description"""

    def __init__(self, msg: str = "No Data Available"):
        Exception.__init__(self, msg)


class IncompatiblePackageVersions(Exception):
    """description"""

    def __init__(self, *packages: Iterable[Union[str, types.ModuleType]], **versions):
        str_o = ", "
        str_l = []

        for p in packages:
            if isinstance(p, str):
                s = f"({p},"
                if p in versions:
                    s += f"{versions[p]}"
                else:
                    s += f"NotSpecified"
                s += ")"
                str_l.append(s)
            elif isinstance(p, types.ModuleType):
                str_l.append(f"{p.__name__, p.__version__}")
        for vk, vv in versions.items():
            if vk not in packages:
                str_l.append(f"({vk},{vv})")

        Exception.__init__(self, f"Packages {str_o.join(str_l)} are not compatible")


if __name__ == "__main__":

    def main() -> None:
        """
        :rtype: None
        """
        raise IncompatiblePackageVersions(
            "numpy",
            "scipy",
            "Something",
            numpy="0.0.1",
            scipy="0.0.2",
            some_other_packge="0.5.0",
        )

    def main2() -> None:
        """
        :rtype: None
        """
        import numpy
        import scipy

        raise IncompatiblePackageVersions(numpy, scipy)

    # main()
    main2()
