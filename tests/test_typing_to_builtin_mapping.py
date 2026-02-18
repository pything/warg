from typing import Tuple

from warg.typing_extension import TYPING_TO_BUILTIN_MAP


def test_tuple_of_str():

    value = ("a",)
    t = Tuple[str, ...]
    builtin_type = TYPING_TO_BUILTIN_MAP.get(t.__name__, t)
    value = builtin_type(value)

    print(value)


def test_tuple_of_str_self():

    value = ("a",)
    t = type(value)
    builtin_type = TYPING_TO_BUILTIN_MAP.get(t.__name__, t)
    value = builtin_type(value)

    print(value)
