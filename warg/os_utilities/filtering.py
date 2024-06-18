#!/usr/bin/env python3

__author__ = "heider"
__doc__ = r"""

           Created on 8/30/22
           """

__all__ = ["is_excluded", "is_python_package", "is_python_module", "negate"]

import logging
import re
from functools import wraps
from pathlib import Path
from typing import Any, Callable, MutableMapping, Sequence, Union

logger = logging.getLogger(__name__)


def is_python_module(path: Path) -> bool:
    """
    Check if path is a python module
    """
    path = Path(path)

    return path.is_file() and path.suffix == ".py"


def is_python_package(path: Path) -> bool:
    """
    Check if path is a python package
    """
    path = Path(path)
    return path.is_dir() and (path / "__init__.py").exists()


def is_excluded(path: Union[Path, str], exclude_pattern: str = "[Ee]xcluded*"):
    """
    is exclude by common pattern or gitignore

    #TODO: Look up nearest parent git ignore and interpret

    :param exclude_pattern:
    :type exclude_pattern:
    :param path:
    :type path:
    :return:
    :rtype:
    """

    if len(re.findall(exclude_pattern, str(path))) > 0:
        return True
    return False


def negate(f: Callable) -> Callable:
    """
    Negate a function return
    """

    assert isinstance(f, Callable), "ensure you did not call the callable with parameters directly"

    @wraps(f)
    def wrapper(*args: Sequence[Any], **kwargs: MutableMapping[str, Any]) -> Any:
        """

        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        return not f(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    # logger.info(negate(is_excluded("/iods/excludes/osad.py")))
    logger.info(negate(is_excluded)("/iods/excludes/osad.py"))
    logger.info(is_excluded("/s/excludes/a.py"))
    logger.info(is_excluded("/s/exclud/a.py"))
    logger.info(is_excluded("/s/exclude/a.py"))
    logger.info(is_excluded("/s/Exclude/a.py"))
    logger.info(is_excluded("/s/excluded/a.py"))
    logger.info(is_excluded("/s/Excluded/a.py"))
