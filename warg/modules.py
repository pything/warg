from pathlib import Path

import importlib
import logging
import pkgutil
from types import ModuleType
from typing import Any, Generator, Union

from warg import ensure_in_sys_path

_logger = logging.getLogger(__name__)


__all__ = ["iter_import_module", "get_submodules", "get_submodules_by_path"]


def iter_import_module(module_name: str, *module_paths: Union[str, Path]) -> Generator[ModuleType, Any, None]:
    _logger.info(f"Found {module_name} in {module_paths}")

    # Ensure paths are strings for pkgutil
    module_str_paths = [str(p) for p in module_paths]

    yield from (
        importlib.import_module(module_info.name)
        for module_info in pkgutil.iter_modules(module_str_paths, prefix=f"{module_name}.")
    )


def get_submodules(module: ModuleType) -> Generator[ModuleType, Any, None]:
    _logger.info(f"Found {module.__path__} {module.__name__}")

    yield from iter_import_module(module.__name__, *module.__path__)


def get_submodules_by_path(module_path: Path) -> Generator[ModuleType, Any, None]:
    a = module_path.resolve(strict=True)

    assert a.exists(), f"{a} does not exist"

    ensure_in_sys_path(module_path.parent)

    yield from iter_import_module(a.stem, a)


if __name__ == "__main__":
    _logger.warning(list(get_submodules_by_path(Path(__file__).parent)))
