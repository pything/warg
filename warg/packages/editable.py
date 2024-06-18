#!/usr/bin/env python3
import json

try:
    from importlib.metadata import Distribution, PackageNotFoundError, PathDistribution
except (ModuleNotFoundError, ImportError) as e:
    from importlib_metadata import Distribution, PackageNotFoundError, PathDistribution

__all__ = [
    "dist_is_editable",
    "package_is_editable",
    "get_dist_package_location",
    "get_package_location",
]

from pathlib import Path
from typing import Optional
import logging

logger = logging.getLogger(__name__)
VERBOSE = False


# noinspection PyProtectedMember
def dist_is_editable(dist: Distribution) -> bool:
    """
    Return True if given Distribution is an editable installation.

    This function might still change alot

    """
    top_level = dist.read_text("top_level.txt")

    top_level_name = None
    if top_level:
        top_level_name = top_level.split("\n")[0].strip()

    else:  # assume top level namespace is the same as dist
        if isinstance(dist, PathDistribution):
            if hasattr(dist, "_normalized_name"):  # This is wacky...
                top_level_name = dist._normalized_name

        elif isinstance(dist, Distribution):
            if hasattr(dist, "name"):
                top_level_name = dist.name

    if top_level_name:
        if hasattr(dist, "_read_files_egginfo"):
            if dist._read_files_egginfo() is not None:
                if top_level_name == dist._path.parent.stem:
                    return True

    if hasattr(dist, "_read_files_distinfo"):
        if dist._read_files_distinfo() is not None:
            direct_url_str = dist.read_text("direct_url.json")
            if direct_url_str is not None:
                direct_url_json = json.loads(direct_url_str)
                if "dir_info" in direct_url_json:
                    if "editable" in direct_url_json["dir_info"]:
                        return direct_url_json["dir_info"]["editable"]

    return False


IGNORE = '''

def dist_is_editable(dist: Any) -> bool:
    """
    Return True if given Distribution is an editable installation."""
    for path_item in sys.path:
        egg_link = Path(path_item) / f"{dist.project_name}.egg-link"
        if egg_link.is_file():
            return True
    return False
'''


def package_is_editable(package_name: str) -> bool:
    """
    Return True if given Package is an editable installation.
    """
    try:
        dist = Distribution.from_name(package_name)

        return dist_is_editable(dist)

    except PackageNotFoundError as p:
        if VERBOSE:
            logger.info(p)


def get_package_location(package_name: str) -> Path:
    try:
        dist = Distribution.from_name(package_name)
        if dist:
            return get_dist_package_location(dist)

    except PackageNotFoundError as p:
        if VERBOSE:
            logger.info(p)


# noinspection PyProtectedMember
def get_dist_package_location(dist: Distribution) -> Optional[Path]:
    """
    FULL OF ASSUMPTIONS!

    :param dist:
    :return:
    """
    top_level = dist.read_text("top_level.txt")

    top_level_name = None
    if top_level:
        top_level_name = top_level.split("\n")[0].strip()

    else:  # assume top level namespace is the same as dist
        if isinstance(dist, PathDistribution):
            if hasattr(dist, "_normalized_name"):  # This is wacky...
                top_level_name = dist._normalized_name

        elif isinstance(dist, Distribution):
            if hasattr(dist, "name"):
                top_level_name = dist.name

    if top_level_name:
        if hasattr(dist, "_read_files_egginfo"):
            if dist._read_files_egginfo() is not None:
                if top_level_name == dist._path.parent.stem:
                    return dist._path.parent

    if hasattr(dist, "_read_files_distinfo"):
        if dist._read_files_distinfo() is not None:
            direct_url_str = dist.read_text("direct_url.json")
            if direct_url_str is not None:
                direct_url_json = json.loads(direct_url_str)
                if "dir_info" in direct_url_json:
                    if "editable" in direct_url_json["dir_info"]:
                        return Path(direct_url_json["url"])

    if top_level_name:
        package_location = dist._path.parent / top_level_name
        if package_location.exists() and package_location.is_dir():
            return package_location

    return None


if __name__ == "__main__":
    logger.info(package_is_editable(package_name="draugr"))
    logger.info(get_package_location(package_name="draugr"))

    logger.info(package_is_editable(package_name="warg"))
    logger.info(get_package_location(package_name="warg"))

    logger.info(package_is_editable(package_name="apppath"))
    logger.info(get_package_location(package_name="apppath"))

    logger.info(get_package_location(package_name="numpy"))

    logger.info(package_is_editable(package_name="Pillow"))
    logger.info(get_package_location(package_name="Pillow"))
    logger.info(get_package_location(package_name="pillow"))
