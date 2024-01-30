from warg import import_submodule_alls

s = import_submodule_alls(__name__)
for s_, v in s.items():
    assert s_ not in vars()
    vars()[s_] = v

__all__ = [*s.keys()]
