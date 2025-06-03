import gc
import os
import shutil
import sys

from pathlib import Path
from stat import filemode

from warg.runtime import unload_modules

if __name__ == "__main__":

    def main():
        # print(sys.modules)

        import some_module

        module_path = Path(some_module.__path__[0])

        # print( os.access(module_path, os.F_OK | os.X_OK))
        shutil.rmtree(module_path)

        if True:
            with os.scandir(module_path) as scandir_it:
                entries = list(scandir_it)
            for entry in entries:
                fullname = entry.path
                try:
                    os.unlink(fullname)
                except Exception as e:
                    print(e)

            os.rmdir(module_path)

        failed = False
        try:
            os.unlink(module_path)
        except PermissionError:
            failed = True

        if not failed:
            raise Exception()

        print(some_module.__doc__)

        print(gc.get_stats())
        # print(gc.get_referrers(some_module))
        # print(gc.get_referents(some_module))
        print(gc.is_tracked(some_module))
        print(gc.is_finalized(some_module))
        # print(gc.get_objects())

        del some_module
        unload_modules()

        # print(sys.meta_path)
        print(gc.garbage)
        print(gc.callbacks)
        # print(gc.get_objects())
        # print(gc.is_finalized())
        gc.collect(generation=2)

        # folder_stat = os.stat(module_path)
        # for mode in (folder_stat.st_mode,):
        #  print(filemode(mode))

        # fd = os.open(module_path, os.O_RDONLY)
        # os.close(fd)

        # print( os.lstat(module_path))

        # print(os.statvfs(module_path))
        # os.unlink(module_path)

        # sys.audit("os.unlink", str(module_path))
        # print(sys.exc_info())

        # sys.audit("shutil.rmtree", str(module_path))

        # remove_tree(module_path,dry_run=True)

        # gc.is_finalized(some_module)

        # print(sys.modules)

    main()
