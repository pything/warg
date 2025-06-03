#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09-09-2020
           """

__all__ = [
    "map_value_product",
    "map_product",
    "map_sorted",
    "map_permutations",
    "map_combinations",
    "map_combinations_with_replacement",
]

import itertools
import logging
from typing import Any, Generator, Mapping, Optional, Tuple

logger = logging.getLogger(__name__)


def map_value_product(mappings: Optional[Mapping]) -> Optional[Generator[dict, None, None]]:
    """

    :param mappings:
    :return:
    """
    if mappings is None:
        return None

    return (dict(zip(mappings, x)) for x in itertools.product(*mappings.values()))


def map_reversed(mapping: Optional[Mapping]) -> Optional[dict]:
    """

    :param mapping:
    :return:
    """
    if mapping is None:
        return None

    return dict(reversed(list(mapping.items())))


def map_sorted(mapping: Optional[Mapping], **kwargs) -> Optional[dict]:
    """

    :param mapping:
    :param kwargs:
    :return:
    """
    if mapping is None:
        return None

    return dict(sorted(mapping.items(), **kwargs))


def map_product(mapping: Mapping, repeat: int = 2) -> Any:
    """description"""
    yield from zip(
        itertools.product(mapping.keys(), repeat=repeat),
        itertools.product(mapping.values(), repeat=repeat),
    )


def map_permutations(mapping: Mapping, repeat: int = 2) -> Generator[Tuple[Any, ...], None, None]:
    """

    :param mapping:
    :param repeat:
    :return:
    """
    yield from zip(
        itertools.permutations(mapping.keys(), repeat),
        itertools.permutations(mapping.values(), repeat),
    )


def map_combinations(mapping: Mapping, repeat: int = 2) -> Generator[Tuple[Any, ...], None, None]:
    """

    :param mapping:
    :param repeat:
    :return:
    """
    yield from zip(
        itertools.combinations(mapping.keys(), repeat),
        itertools.combinations(mapping.values(), repeat),
    )


def map_combinations_with_replacement(
    mappings: Mapping, repeat: int = 2
) -> Generator[Tuple[Any, ...], None, None]:
    """

    :param mappings:
    :param repeat:
    :return:
    """
    if mappings is None:
        return None

    yield from zip(
        itertools.combinations_with_replacement(mappings.keys(), repeat),
        itertools.combinations_with_replacement(mappings.values(), repeat),
    )


if __name__ == "__main__":

    def asdijha() -> None:
        """
        :rtype: None
        """
        from warg import NOD

        a = NOD(a=[1], b=[4], c=[8])
        logger.info(f"ValueMapProduct{str(list(map_value_product(a.as_dict())))}")
        logger.info(f"MapProduct{str(list(map_product(a.as_dict())))}")
        logger.info(f"map_combinations{str(list(map_combinations(a.as_dict())))}")
        logger.info(f"map_permutations{str(list(map_permutations(a.as_dict())))}")
        logger.info(
            f"map_combinations_with_replacement{str(list(map_combinations_with_replacement(a.as_dict())))}"
        )

    def asdijhsadasdad() -> None:
        """
        :rtype: None
        """
        from warg import NOD

        a = NOD(a=[1, 2, 8], b=[4, 3, 99])
        logger.info(f"ValueMapProduct{str(list(map_value_product(a.as_dict())))}")
        logger.info(f"MapProduct{str(list(map_product(a.as_dict())))}")
        logger.info(f"map_combinations{str(list(map_combinations(a.as_dict())))}")
        logger.info(f"map_permutations{str(list(map_permutations(a.as_dict())))}")
        logger.info(
            f"map_combinations_with_replacement{str(list(map_combinations_with_replacement(a.as_dict())))}"
        )

    asdijha()
    # asdijhsadasdad()
