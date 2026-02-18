__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 18/07/2020
           """

__all__ = [
    "Number",
    "Reals",
    "Numbers",
    "Single",
    "Double",
    "Triple",
    "Quad",
    "Quint",
    "SingleNumber",
    "DoubleNumber",
    "TripleNumber",
    "QuadNumber",
    "QuintNumber",
    "StrictNumbers",
    "is_collection_of_strings",
    "is_union",
    "is_optional",
    "get_args",
    "get_origin",
    "TYPING_TO_BUILTIN_MAP",
]

import numbers
from typing import Any, Sequence, Tuple, Union, Generic, ParamSpecArgs, ParamSpecKwargs, Union

try:  # Python >= 3.8
    from typing import Literal, get_args, get_origin

except ImportError:  # Compatibility
    get_args = lambda t: getattr(t, "__args__", ()) if t is not Generic else Generic
    get_origin = lambda t: getattr(t, "__origin__", None)


def is_union(field: Union[ParamSpecArgs, ParamSpecKwargs]) -> bool:
    """

    :param field:
    :type field:
    :return:
    :rtype:
    """
    return get_origin(field) is Union


def is_optional(field: Union[ParamSpecArgs, ParamSpecKwargs]) -> bool:
    """

    :param field:
    :type field:
    :return:
    :rtype:
    """
    return is_union(field) and type(None) in get_args(field)


Number = Union[int, float]
Reals = Sequence[Union[numbers.Real, "Reals"]]
Numbers = Sequence[Union[Number, "Numbers"]]
StrictNumbers = Union[Union[Sequence[int], "StrictNumbers"], Union[Sequence[float], "StrictNumbers"]]

Single = Tuple[Any]
Double = Tuple[Any, Any]
Triple = Tuple[Any, Any, Any]
Quad = Tuple[Any, Any, Any, Any]
Quint = Tuple[Any, Any, Any, Any, Any]

SingleNumber = Tuple[Number]
DoubleNumber = Tuple[Number, Number]
TripleNumber = Tuple[Number, Number, Number]
QuadNumber = Tuple[Number, Number, Number, Number]
QuintNumber = Tuple[Number, Number, Number, Number, Number]


def is_collection_of_strings(ano: type) -> bool:
    """
    function to check if a type annotation is a collection of strings, like List[str], Tuple[str, ...], Set[str], or their non-typing equivalents list, tuple, set with str as the only element

    :param ano:
    :type ano:
    :return:
    :rtype:
    """
    return (isinstance(ano, type) and issubclass(ano, (tuple, list, set))) or (
        get_origin(ano) in (tuple, list, set) and get_args(ano) and get_args(ano)[0] == str
    )


if __name__ == "__main__":

    def stest() -> None:
        """
        :rtype: None
        """
        assert (
            isinstance(1, Number.__args__)
            and isinstance(1.1, Number.__args__)
            and not isinstance(complex(1, 1), Number.__args__)
        )
        # assert isinstance(list(range(2)), Numbers.__args__) and isinstance((float(i) for i in range(2)), Numbers.__args__) and isinstance((1,2.0), Numbers.__args__)
        # assert isinstance(list(range(2)), StrictNumbers.__args__) and isinstance((float(i) for i in range(2)), StrictNumbers.__args__) and not isinstance((1,2.0), StrictNumbers.__args__)
        assert (
            isinstance(1, numbers.Real)
            and isinstance(1.1, numbers.Real)
            and not isinstance(complex(2, 2), numbers.Real)
        )
        # assert isinstance(list(range(2)), Reals.__args__) and isinstance((float(i) for i in range(2)), Reals.__args__) and isinstance((1,2.0), Reals.__args__)

    stest()
TYPING_TO_BUILTIN_MAP = {
    # Collection types
    "Tuple": tuple,
    "List": list,
    "Dict": dict,
    "Set": set,
    "FrozenSet": frozenset,
    # Mapping types
    "Mapping": dict,
    "MutableMapping": dict,
    "OrderedDict": dict,
    "ChainMap": dict,
    # Sequence types
    "Sequence": list,
    "MutableSequence": list,
    "Deque": list,
    # Set types
    "AbstractSet": set,
    "MutableSet": set,
}
