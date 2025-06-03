#!/usr/bin/env python3


__project__ = "Warg"

__author__ = "Christian Heider Lindbjerg"
__version__ = "1.4.9"
__doc__ = r"""
Created on 27/04/2019

@author: cnheider

"""

from pathlib import Path

import logging

logger = logging.getLogger(__name__)

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

# with open(Path(__file__).parent.parent / "README.md", "r") as this_init_file:
#    __doc__ += this_init_file.read()

# __all__ = ["PROJECT_APP_PATH", "PROJECT_NAME", "PROJECT_VERSION", "get_version"] # let everything be accessible
# from base warg import

try:
    # from .ode import * # Silly thing
    from .data_structures import *
    from .arguments import *
    from .gdkc import *
    from .mixins import *
    from .decorators import *
    from .metas import *
    from .bases import *
    from .typing_extension import *
    from .context_wrapper import *
    from .boolean_tests import *
    from .map_itertools import *
    from .ast_ops import *
    from .functions import *
    from .os_utilities import *
    from .generators import *
    from .text import *
    from .math_utilities import *
    from .business import *
    from .datetimes import *
    from .debug import *
    from .exceptions import *
    from .manipulation import *
    from .replication import *
    from .strings import *
    from .contexts import *
    from .config_shell import *
    from .colors import *
    from .packages import *
    from .iteration import *
    from .logging_utilities import *
    from .modules import *
except ImportError as ix:
    this_package_name = Path(__file__).parent.name
    this_package_reqs = Path(__file__).parent.parent / f"requirements.txt"
    if this_package_reqs.exists():
        logger.info(
            f"Make sure requirements is installed for {this_package_name}, see {this_package_reqs}"
        )  # TODO: PARSE WHAT is missing and print
    raise ix

PROJECT_NAME = clean_string(__project__)
PROJECT_VERSION = __version__
PROJECT_YEAR = 2018
PROJECT_AUTHOR = clean_string(__author__)
PROJECT_ORGANISATION = clean_string("Pything")

__url__ = f"https://github.com/{PROJECT_ORGANISATION}/{PROJECT_NAME}"

# from apppath import AppPath # CAREFUL CIRCULAR DEPENDENCY WARNING!
# PROJECT_APP_PATH = AppPath(app_name=PROJECT_NAME, app_author=PROJECT_AUTHOR) # NOT USED!

import_issue_found = False
try:
    from importlib.resources import files
    from importlib.metadata import PackageNotFoundError
except:
    try:
        from importlib_metadata import PackageNotFoundError
        from importlib_resources import files
    except:
        import_issue_found = True

if import_issue_found:
    PACKAGE_DATA_PATH = Path(__file__).parent / "data"
    DEVELOP = False
else:
    PACKAGE_DATA_PATH = files(PROJECT_NAME) / "data"

    try:
        DEVELOP = package_is_editable(PROJECT_NAME)
    except PackageNotFoundError as e:
        DEVELOP = True

__version__ = get_version(__version__, append_time=DEVELOP)
__version_info__ = tuple(int(segment) for segment in __version__.split("."))

if __name__ == "__main__":
    logger.info(__version__)
