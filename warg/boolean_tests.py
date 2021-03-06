#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 02/01/2020
           """

__all__ = [
    "is_positive_and_mod_zero",
    "is_zero_or_mod_zero",
    "is_none_or_zero_or_negative",
    "is_zero_or_mod_below",
    "is_none_or_zero_or_negative_or_mod_zero",
]

from typing import Any

from warg.decorators import drop_unused_kws, passes_kws_to


@drop_unused_kws
def is_positive_and_mod_zero(
    mod: int, counter: int, *, ret: Any = True, alt: Any = False
) -> Any:
    """

    test if mod is positive
    then test if counter % mod is 0
    if both tests are true return ret
    else return alt


    @param mod:
    @param counter:
    @param ret:
    @param alt:
    @return:"""

    return ret if (mod > 0 and (counter % mod == 0)) else alt


@drop_unused_kws
def is_zero_or_mod_below(
    mod: int, below: int, counter: int, *, ret: Any = True, alt: Any = False
) -> Any:
    """

    test if mod is zero or if counter % mod is 0
    if any of the tests are true return ret
    else return alt


    @param below:
    @type below:
    @param mod:
    @param counter:
    @param ret:
    @param alt:
    @return:"""
    return ret if (mod == 0 or (counter % mod < below)) else alt


@drop_unused_kws
def is_zero_or_mod_zero(
    mod: int, counter: int, *, ret: Any = True, alt: Any = False
) -> Any:
    """

    test if mod is zero or if counter % mod is 0
    if any of the tests are true return ret
    else return alt


    @param mod:
    @param counter:
    @param ret:
    @param alt:
    @return:"""
    return ret if (mod == 0 or (counter % mod == 0)) else alt


def is_none_or_zero_or_negative(obj: Any) -> bool:
    """

    @param obj:
    @return:"""
    is_none = obj is None
    is_negative = False
    if isinstance(obj, (int, float)):
        is_negative = obj <= 0

    return is_none or is_negative


@passes_kws_to(is_zero_or_mod_zero)
def is_none_or_zero_or_negative_or_mod_zero(mod: int, counter: int, **kwargs) -> bool:
    """

    @param mod:
    @param counter:
    @param kwargs:
    @return:"""
    return is_none_or_zero_or_negative(mod) or is_zero_or_mod_zero(
        mod, counter, **kwargs
    )


if __name__ == "__main__":
    assert is_zero_or_mod_below(5, 3, 7) == True
    assert is_zero_or_mod_below(5, 2, 4) == False
    for i in range(9):
        print(is_zero_or_mod_zero(1, i))
    for i in range(9):
        print(is_zero_or_mod_zero(2, i))

    print()
    for i in range(8):
        print(is_none_or_zero_or_negative_or_mod_zero(None, i))
