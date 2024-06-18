import logging
from typing import Any, Iterable, Union

logger = logging.getLogger(__name__)


def to_string_if_not_of_exact_type(gen: Iterable, type_: Iterable[type] = (int, float)) -> Union[str, Any]:
    """

    :param type_: Type for testing against
    :param gen: The iterable to be converted
    :return:
    """
    if not isinstance(type_, Iterable):
        type_ = [type_]

    for v in gen:
        if all([type(v) != t for t in type_]):
            yield str(v)
        else:
            yield v


def solve_type(d: Any) -> str:
    """
    Does not support size/length yet...

    :param d:
    :return:
    """
    if not isinstance(d, bool):
        if isinstance(d, int):
            return "integer"

        elif isinstance(d, float):
            return "double"

    return "string"


if __name__ == "__main__":
    logger.info(solve_type(True))

    logger.info(list(to_string_if_not_of_exact_type([True, 1, "A", 2.0])))
