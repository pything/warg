#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 01/08/2020
           """

import logging

logger = logging.getLogger(__name__)
__all__ = []

from pathlib import Path


def test_import():
    import warg

    logger.info(warg.__version__)


def test_find_nearest_ancestral_relative():
    from warg import find_nearest_ancestral_relative

    assert (
        find_nearest_ancestral_relative(
            "scripts",
            top_level=Path(__file__).parent.parent,
            context=Path(__file__),
            ancestral_levels=2,
            descendant_levels=1,
        )
        == Path(__file__).parent.parent
    )


def test_find_ancestral_relatives():
    from warg import find_ancestral_relatives

    assert find_ancestral_relatives(
        "warg",
        top_level=Path(__file__).parent.parent,
        context=Path(__file__),
        ancestral_levels=1,
        descendant_levels=1,
    ) == [Path(__file__).parent.parent]
