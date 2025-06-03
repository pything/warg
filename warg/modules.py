import importlib
import logging
import pkgutil
from pathlib import Path
from types import ModuleType
from typing import Any, Generator, Sequence

logger = logging.getLogger(__name__)


__all__ = ["iter_import_module", "get_submodules", "get_submodules_by_path"]


def iter_import_module(module_name: str, module_paths: Sequence[str]) -> Generator[ModuleType, Any, None]:
    logger.info(f"Found {module_name} in {module_paths}")

    yield from (
        importlib.import_module(f"{module_name}.{module_info.name}")
        for module_info in pkgutil.iter_modules(module_paths)
    )


def get_submodules(module: ModuleType) -> Generator[ModuleType, Any, None]:
    logger.info(f"Found {module.__path__} {module.__name__}")

    yield from iter_import_module(module.__name__, module.__path__)


def get_submodules_by_path(module_path: Path) -> Generator[ModuleType, Any, None]:
    assert module_path.exists(), f"{module_path} does not exist"

    yield from iter_import_module(module_path.stem, [str(module_path)])
