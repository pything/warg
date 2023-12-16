#!/usr/bin/env python3

__doc__ = r"""

           Created on 17/02/2020
           """

__author__ = "Christian Heider Lindbjerg"

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .dict_mixins import *
from .ordinal_index_mixin import *
from .private import *
