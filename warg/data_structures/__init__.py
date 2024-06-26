#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 06-11-2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .auto_dict import *
from .named_ordered_dictionary import *
from .ordered_set import *
from .sequences import *
from .mappings import *
