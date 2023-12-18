#!/usr/bin/env python3

from typing import Callable, Iterable, List, Sequence, Any, Tuple

__all__ = ["pairs", "chunks", "leaf_apply", "leaf_type_apply"]


def pairs(s: Sequence) -> Tuple[Any, Any]:
    """
    Iterate over a list in overlapping pairs.

    Usage:
        lst = [4, 7, 11, 2]
        pairs(lst) yields (4, 7), (7, 11), (11, 2)

    https://stackoverflow.com/questions/1257413/1257446#1257446


    :param s: An iterable/list
    :return: Yields a pair of consecutive elements (lst[k], lst[k+1]) of lst. Last call yields (lst[-2], lst[-1]).
    """
    i = iter(s)
    prev = next(i)

    for item in i:
        yield prev, item
        prev = item


def leaf_apply(seq: Iterable, func: Callable) -> List:
    sub = []
    for element in seq:
        if isinstance(element, Iterable):
            sub.append(leaf_apply(element, func))
        else:
            sub.append(func(element))
    return sub


def leaf_type_apply(seq: Iterable, func: Callable, leaf_type: type = tuple) -> List:
    sub = []
    for element in seq:
        if not isinstance(element, leaf_type):
            sub.append(leaf_type_apply(element, func, leaf_type))
        else:
            sub.append(func(element))
    return sub


def chunks(lst: Sequence, n: int) -> Any:
    """
    Yield successive n-sized chunks from lst.

     :param lst:
     :param n:
     :return:
    """
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


if __name__ == "__main__":
    print(list(chunks(list(range(10)), 3)))
