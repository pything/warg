#!/usr/bin/env python3

__all__ = ["get_version"]

import datetime
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class NotGitException(Exception):
    pass


def get_version(version: str, append_time: bool = False, verbose: bool = False, context: Path = None) -> str:
    """

    :param context:
    :param verbose:
    :param version:
    :param append_time:
    :return:
    """

    if not version:
        version = "0.0.0"

    try:
        import subprocess

        if context is None:
            import inspect
            import os

            caller_parent = Path(os.path.abspath((inspect.stack()[1])[1])).resolve().parent

        else:
            context = Path(context)
            if context.is_file():
                caller_parent = context.parent
            else:
                caller_parent = context

        if (caller_parent / ".git").exists() and (caller_parent / ".git").is_dir():
            git_version = (
                subprocess.check_output(
                    [
                        "git",
                        "describe",
                        "--always",
                        # "--dirty",
                        "origin/HEAD",
                    ],
                    cwd=caller_parent,
                )
                .strip()
                .decode()
            )

            current_git_version = (
                subprocess.check_output(
                    [
                        "git",
                        "describe",
                        "--always",
                        "--dirty",
                    ],
                    cwd=caller_parent,
                )
                .strip()
                .decode()
            )

            if "dirty" in current_git_version:
                logger.warning(f"{caller_parent} git is dirty, {current_git_version}")

            if git_version.split("-")[0] != version:
                msg = f"{caller_parent} git version {git_version} does not match __version__" f" {version}"
                logger.warning(msg)
                assert git_version.split("-")[0] == version, msg

            else:
                if verbose:
                    msg = f"{caller_parent} git version {git_version} matches __version__" f" {version}"
                    logger.info(msg)

        else:
            raise NotGitException

    except:
        if append_time:
            try:
                now = datetime.datetime.now(datetime.UTC)
            except:
                now = datetime.datetime.utcnow()
            date_version = now.strftime("%Y%m%d%H%M%S")
            # date_version = time.time()

            if version:
                # Most git tags are prefixed with 'v' (example: v1.2.3) this is
                # never desirable for artefact repositories, so we strip the
                # leading 'v' if it's present.
                version = version[1:] if isinstance(version, str) and version.startswith("v") else version
            else:
                # The Default version is an ISO8601 compliant datetime. PyPI doesn't allow
                # the colon ':' character in its versions, and time is required to allow
                # for multiple publications to master in one day. This datetime string
                # uses the 'basic' ISO8601 format for both its date and time components
                # to avoid issues with the colon character (ISO requires that date and
                # time components of a date-time string must be uniformly basic or
                # extended, which is why the date component does not have dashes.)
                #
                # Publications using datetime versions should only be made from master
                # to represent the HEAD moving forward.
                logger.warning(
                    f"Environment variable VERSION is not set, only using datetime: {date_version}"
                )

                # warn(f'Environment variable VERSION is not set, only using timestamp: {version}')

            version = f"{version}.{date_version}"

    return version


if __name__ == "__main__":
    from warg import __version__

    logger.info(__version__)
    logger.info(get_version("1.2.7", verbose=True))
