#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 16/02/2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .caching import *
from .hashing import *
from .kw_passing import *
from .timing import *
from .exporting import *
from .wrapping import *
