__all__ = ["unload_modules"]

import importlib
import sys

BUILT_IN = [*sys.builtin_module_names, *sys.stdlib_module_names]


def unload_modules(*modules: str) -> None:
    if not modules:
        modules = sys.modules.copy()

    for sm in modules.keys():
        if sm in BUILT_IN:
            continue

        del sys.modules[sm]

        for mod in modules.values():
            try:
                delattr(mod, sm)
            except AttributeError:
                pass

    importlib.invalidate_caches()
    # sys._clear_internal_caches()


if __name__ == "__main__":

    def main():
        import argparse

        print(argparse)

        unload_modules()

        print(sys.modules)

    main()
