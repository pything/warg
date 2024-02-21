#!/usr/bin/env python3

__doc__ = r"""

           Created on 31/07/2023
           """

__author__ = "Christian Heider Lindbjerg"

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()

from .pip_parsing import *
from .reloading import *
from .editable import *
from .versioning import *
from .namespaces import *
from .satisfaction import *
