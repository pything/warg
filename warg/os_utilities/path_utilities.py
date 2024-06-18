#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 07-05-2021
           """

import logging
import os
import subprocess
from pathlib import Path
from typing import Optional

from warg.os_utilities.os_platform import has_x_server, is_mac, is_windows

logger = logging.getLogger(__name__)
__all__ = ["latest_file", "exist_any_extension", "system_open_path"]


def system_open_path(path: Path, *, verbose: bool = False) -> None:
    """
    Use system defaults for opening path/uris

    :param path:
    :type path:
    :param verbose:
    :type verbose:
    :return:
    :rtype:
    """
    if has_x_server():
        if verbose:
            logger.info(f"Opening ({path}) using the systems default handler")

        if is_windows():
            if path.is_dir():
                subprocess.Popen(["start", path], shell=True)
            else:
                os.startfile(path, "open")

        elif is_mac():
            subprocess.Popen(["open", path])

        else:
            # try:
            subprocess.Popen(["xdg-open", path])
            # except OSError:
    else:
        logger.info("Target display not set")


def latest_file(
    directory: Path,
    extension: str = "",
    *,
    recurse: bool = False,
    raise_on_failure: bool = True,
) -> Optional[Path]:
    """

    :param directory:
    :param extension:
    :param recurse:
    :param raise_on_failure:
    :return:
    """
    a = f"*{extension}"
    if recurse:
        path_gen = directory.rglob(a)
    else:
        path_gen = directory.glob(a)
    list_of_files = list(path_gen)
    if len(list_of_files) == 0:
        msg = f"Found no previous files with extension {extension} in {directory}"
        if raise_on_failure:
            raise FileNotFoundError(msg)
        logger.info(f"{msg}, returning None!")
        return
    return max(list_of_files, key=os.path.getctime)  # USES CREATION TIME


def exist_any_extension(p: Path) -> bool:
    """
    If any file with that stem exists in the parent directory, return True.

    :param p:
    :type p:
    :return:
    :rtype:
    """
    for _ in p.parent.glob(f"{p.stem}.*"):
        return True
    return False


if __name__ == "__main__":
    logger.info(latest_file(Path(__file__).parent, recurse=True))
    logger.info(exist_any_extension(Path(__file__)))
    logger.info(exist_any_extension(Path.cwd() / "__init__.py"))
    logger.info(exist_any_extension(Path.cwd() / "__init__"))
    logger.info(exist_any_extension(Path.cwd() / "__init__.test"))
    logger.info(exist_any_extension(Path.cwd() / "__init___.py"))

    system_open_path(Path("__init__.py"))
    # system_open_path(Path(__file__).parent)
