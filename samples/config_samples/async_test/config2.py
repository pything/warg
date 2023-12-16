#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 11-12-2020
           """

from pathlib import Path

from warg import import_warning

import_warning(Path(__file__).with_suffix("").name)

A_CONSTANT = 2
ANOTHER_CONSTANT = 42
