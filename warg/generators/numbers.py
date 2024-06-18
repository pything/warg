#!/usr/bin/env python3
import random
from typing import Callable, Iterable, List, Optional, Tuple

from warg import Number

__all__ = ["n_uint_mix", "n_uint_mix_generator_builder", "n_uint_mix_generator"]


import logging

logger = logging.getLogger(__name__)


def n_uint_mix(mix_max: Iterable[Number], mix_min: Optional[Iterable[Number]] = None) -> List[Number]:
    mix_max = list(mix_max)

    if mix_min is None:
        mix_min = [0] * len(mix_max)

    assert len(mix_min) == len(mix_max)

    for min_, max_ in zip(mix_min, mix_max):
        assert min_ <= max_

    return [random.randrange(min_, max_) for min_, max_ in zip(mix_min, mix_max)]


def n_uint_mix_generator(*mix, mix_min: Optional[Iterable[Number]] = None) -> Tuple[Number, ...]:
    if len(mix) == 1:
        if isinstance(mix, Iterable):
            mix = mix[0]

    while 1:
        yield n_uint_mix(mix, mix_min=mix_min)


def n_uint_mix_generator_builder(*mix: Number, mix_min: Optional[Iterable[Number]] = None) -> Callable:
    """Compatability code.."""

    if len(mix) == 1:
        if isinstance(mix, Iterable):
            mix = mix[0]

    def no_arg_generator() -> Tuple[Number, ...]:
        while 1:
            yield n_uint_mix(mix, mix_min=mix_min)

    return no_arg_generator


if __name__ == "__main__":
    logger.info([v for _, v in zip(range(9), iter(n_uint_mix_generator(255, 255)))])
    print([v for _, v in zip(range(9), iter(n_uint_mix_generator(255, 255, mix_min=(200, 200))))])
