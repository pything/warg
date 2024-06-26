#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 21/12/2019
           """

from warg import AutoDict, recursive_default_dict_print, sanitise_auto_dict

import logging

logger = logging.getLogger(__name__)


def test_a():
    ad = AutoDict()

    ad["b"]["b"]["c"]["b"]["c"] = {}
    ad["c"] = 1
    ad["cd"]["v"] = 412
    ad["qc"]["d"] = []
    ad["cf"]["b6"] = None
    ad["cf"]["1"] = None

    a = ad["b"]["b"]["b"]["b"]
    b = ad["b"]["a"]["gf"]["c"]
    c = ad["cd"]["v"]

    logger.info(a, b, c)

    logger.info(ad)

    recursive_default_dict_print(ad)

    d = sanitise_auto_dict(ad)
    try:
        a = d["b"]["b"]["b"]["b"]
    except KeyError as k:
        assert isinstance(k, KeyError)

    try:
        b = d["b"]["a"]["gf"]["c"]
    except KeyError as k:
        assert isinstance(k, KeyError)

    c = d["cd"]["v"]

    assert c == 412

    logger.info(d)


if __name__ == "__main__":
    test_a()
