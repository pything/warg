import importlib
import logging
import pkgutil
from types import ModuleType
from typing import Any, Dict

logger = logging.getLogger(__name__)
__all__ = ["import_submodules", "import_submodule_alls"]


def import_submodules(package: Any, recursive: bool = True) -> Dict[str, ModuleType]:
    """Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :param recursive:
    """

    if isinstance(package, str):
        if package == "__main__":
            assert NotImplementedError
        else:
            package = importlib.import_module(package)

    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = f"{str(package.__name__)}.{str(name)}"
        results[full_name] = importlib.import_module(full_name)

        if recursive and is_pkg:
            results.update(import_submodules(full_name))

    return results


def import_submodule_alls(package: Any) -> Dict[str, ModuleType]:
    """Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :param recursive:
    """

    if isinstance(package, str):
        if package == "__main__":
            assert NotImplementedError
        else:
            package = importlib.import_module(package)

    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = f"{str(package.__name__)}.{str(name)}"
        sub_module = importlib.import_module(full_name)
        if hasattr(sub_module, "__all__"):
            alls = sub_module.__all__
        else:
            alls = dir(sub_module)
        for a in alls:
            results[a] = getattr(sub_module, a)

    return results
