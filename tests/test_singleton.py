#!/usr/bin/env python3
from warg.metas.singleton import SingletonBase, SingletonMeta

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""
           """


import logging

logger = logging.getLogger(__name__)


def test_singleton_class():
    class SingletonBaseClass(SingletonBase):
        pass

    class S1(SingletonBaseClass):
        pass

    a = SingletonBaseClass()
    b = S1()

    assert id(a) == id(b) == id(SingletonBaseClass())


def test_singleton_meta():
    class SingletonBaseMeta(metaclass=SingletonMeta):
        pass

    class S2(SingletonBaseMeta):
        pass

    a = SingletonBaseMeta()
    b = S2()

    assert (id(a) == id(SingletonBaseMeta())) != (id(b) == S2())
