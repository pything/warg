#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 16/02/2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .cyclic_generators import *
from .filtering import *
from .mapping_generator import *
from .zipping_generator import *
from .numbers import *
from .testing import *
