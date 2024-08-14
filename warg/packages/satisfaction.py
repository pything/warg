#!/usr/bin/env python3

__author__ = "heider"
__doc__ = r"""

           Created on 12/19/22
           """

__all__ = [
    "install_requirements_from_file",
]

import logging

import os
import subprocess
import sys
from enum import Enum, auto
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# from warg import is_windows # avoid dependency import not standard python pkgs.
CUR_OS = sys.platform
IS_WIN = any(CUR_OS.startswith(i) for i in ["win32", "cygwin"])
IS_MAC = CUR_OS.startswith("darwin")
VERBOSE = False


# @passes_kws_to(subprocess.check_call)
def catching_callable(*args, **kwargs) -> None:
    try:
        # subprocess.check_call(*args, **kwargs)
        output = subprocess.check_output(*args, **kwargs)
        # subprocess.run(*args,**kwargs)
    except subprocess.CalledProcessError as e:
        output = (e.stderr, e.stdout, e)
    logger.warning(output)


SP_CALLABLE = catching_callable  # subprocess.call
DEFAULT_PIP_INDEX = os.environ.get("PIP_INDEX_URL", "https://pypi.org/pypi/")


class InstallStrategyEnum(Enum):
    """ """

    uninstall_first = auto()  # TODO: HOW MANY TIME TO DO THIS?
    just_install = auto()


def is_pip_installed() -> bool:
    pip_present = True
    try:
        import pip
    except ImportError:
        pip_present = False
    return pip_present


def get_embedded_python_interpreter_path() -> Optional[Path]:
    """

    :return: The path of the qgis python interpreter
    :rtype: Optional[Path]
    """
    interpreter_path = Path(sys.executable)
    fallback = True

    if IS_WIN:
        try_path = interpreter_path.parent / "python.exe"
        if not try_path.exists():
            try_path = interpreter_path.parent / "python3.exe"
            if not try_path.exists():
                logger.error(f"Could not find python {try_path}")
                if not fallback:
                    return None
            else:
                return try_path
        else:
            return try_path

    elif IS_MAC:
        try_path = interpreter_path.parent / "bin" / "python"
        if not try_path.exists():
            try_path = interpreter_path.parent / "bin" / "python3"
            if not try_path.exists():
                logger.error(f"Could not find python {try_path}")
                if not fallback:
                    return None
            else:
                return try_path
        else:
            return try_path

    return interpreter_path


def install_pip_if_not_present(
    always_upgrade: bool = True, install_strategy: InstallStrategyEnum = InstallStrategyEnum.just_install
) -> None:
    if install_strategy == InstallStrategyEnum.uninstall_first:
        ...  # TODO: Implement

    if not is_pip_installed() or always_upgrade:
        if False:
            import ensurepip

            ensurepip.bootstrap(upgrade=True)
        else:
            SP_CALLABLE(
                [
                    str(get_embedded_python_interpreter_path()),
                    "-m",
                    "ensurepip",
                    "--upgrade",
                ]
            )


class UpgradeStrategyEnum(Enum):
    """
    eager - all packages will be upgraded to the latest possible version. It should be noted here that pip’s current
    resolution algorithm isn’t even aware of packages other than those specified on the command line, and those
    identified as dependencies. This may or may not be true of the new resolver.

    only-if-needed - packages are only upgraded if they are named in the pip command or a requirement file (i.e,
    they are direct requirements), or an upgraded parent needs a later version of the dependency than is currently
    installed.

    to-satisfy-only (undocumented, please avoid) - packages are not upgraded (not even direct requirements) unless the
    currently installed version fails to satisfy a requirement (either explicitly specified or a dependency).

    This is actually the “default” upgrade strategy when --upgrade is not set, i.e. pip install AlreadyInstalled and pip
    install --upgrade --upgrade-strategy=to-satisfy-only AlreadyInstalled yield the same behavior.
    """

    eager = "eager"
    to_satisfy_only = "to-satisfy-only"
    only_if_needed = "only-if-needed"


# subprocess.Popen(**ADDITIONAL_PIPE_KWS)
# ADDITIONAL_PIPE_KWS = dict(stderr=subprocess.PIPE,stdout=subprocess.PIPE, stdin=subprocess.PIPE)


def pip_programmatic_install2(package: str) -> None:
    """
    not supported
    :param package:
    :return:
    """
    import importlib

    try:
        importlib.import_module(package)
    except ImportError:
        import pip

        if hasattr(pip, "main"):
            pip.main(["install", package])
        else:
            pip._internal.main(["install", package])
    finally:
        globals()[package] = importlib.import_module(package)
        import site
        from importlib import reload

        reload(site)


def install_requirements_from_file(
    requirements_path: Path,
    upgrade: Optional[bool] = None,
    upgrade_strategy: UpgradeStrategyEnum = UpgradeStrategyEnum.only_if_needed,
) -> None:
    """
    Install requirements from a requirements.txt file.

    :param upgrade:
    :param upgrade_strategy:
    :param requirements_path: Path to requirements.txt file.
    :rtype: None
    """
    requirements_file_parent_directory = str(requirements_path.parent.as_posix())

    os.environ["REQUIREMENTS_FILE_PARENT_DIRECTORY"] = requirements_file_parent_directory

    req_path_str = str(requirements_path)

    args = ["install", "-r", req_path_str]

    if True:  # No progress bar
        args += ["--progress-bar", "off"]

    if True:
        args += ["--user"]

    if upgrade:
        args += ["--upgrade"]

    if True:
        args += ["--ignore-installed"]

    if upgrade_strategy:
        args += ["--upgrade-strategy", upgrade_strategy.value]

    if False:
        import pip

        pip.main(args)

    elif False:
        SP_CALLABLE(["pip"] + args)

    elif True:
        install_pip_if_not_present()

        if is_pip_installed():
            SP_CALLABLE([str(get_embedded_python_interpreter_path()), "-m", "pip", *args])

        else:
            logger.info("PIP IS STILL MISSING!")


if __name__ == "__main__":
    logger.info(get_embedded_python_interpreter_path())
