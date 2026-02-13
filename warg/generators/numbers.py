import random
from typing import Any, Callable, Generator, Iterable, List, Never, Optional, Tuple

from warg import Number

__all__ = ["n_uint_mix", "n_uint_mix_generator_builder", "n_uint_mix_generator", "frange"]


import logging

_logger = logging.getLogger(__name__)


def n_uint_mix(mix_max: Iterable[Number], mix_min: Optional[Iterable[Number]] = None) -> List[Number]:
    mix_max = list(mix_max)

    if mix_min is None:
        mix_min = [0] * len(mix_max)

    assert len(mix_min) == len(mix_max)

    for min_, max_ in zip(mix_min, mix_max):
        assert min_ <= max_

    return [random.randrange(min_, max_) for min_, max_ in zip(mix_min, mix_max)]


def n_uint_mix_generator(
    *mix, mix_min: Optional[Iterable[Number]] = None
) -> Generator[list[int | float], Any, Never]:
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

    def no_arg_generator() -> Generator[list[int | float], Any, Never]:
        while 1:
            yield n_uint_mix(mix, mix_min=mix_min)

    return no_arg_generator


def frange(start: Number, stop: Number, step: Number) -> Generator[Number, None, None]:
    """

    :param start:
    :type start:
    :param stop:
    :type stop:
    :param step:
    :type step:
    """
    while start < stop:
        yield start
        start += step
    yield stop


if __name__ == "__main__":
    _logger.info([v for _, v in zip(range(9), iter(n_uint_mix_generator(255, 255)))])
    print([v for _, v in zip(range(9), iter(n_uint_mix_generator(255, 255, mix_min=(200, 200))))])
