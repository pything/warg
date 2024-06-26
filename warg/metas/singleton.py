#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = """
Created on 27/04/2019

@author: cnheider
"""

__all__ = ["SingletonBase", "SingletonMeta", "key_singleton", "singleton"]

import functools
import logging
from functools import wraps
from typing import Any, Callable, MutableMapping, Sequence

logger = logging.getLogger(__name__)


class SingletonBase:
    """
    A base class for creating singleton class where all subtypes(Derivations) should also return the first
    and only
    instantiation of a particular singleton base type, if this property is not wanted consider using the
    SingletonMeta class instead."""

    instance = None

    def __new__(cls, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)

        return cls.instance


class SingletonMeta(type):
    """
    Conversely the SingletonBase, this base meta class is used for creating singleton class where all
    subtypes(
    Deriavations) should only
    return
    singleton instantiations of a particular singleton type independantly of subtyping and super-types,
    if this property is not
    wanted
    consider using
    the
    SingletonBase class instead."""

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.instance = None

    def __call__(cls, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


def singleton(cls):
    """Use class as singleton."""

    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls_, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
        """

        :param cls_:
        :param args:
        :param kwargs:
        :return:
        """
        it = cls_.__dict__.get("__it__")
        if it is not None:
            return it

        cls_.__it__ = it = cls_.__new_original__(cls_, *args, **kwargs)
        it.__init_original__(*args, **kwargs)
        return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__

    return cls


def key_singleton(cache_key: Any) -> Callable:
    """
    TODO: finish
    """

    def inner_fn(fn: Callable) -> Any:
        """description"""

        @wraps(fn)
        def wrapper(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
            """description"""
            instance = getattr(self, cache_key)
            if instance is not None:
                return instance

            instance = fn(self, *args, **kwargs)
            setattr(self, cache_key, instance)
            return instance

        return wrapper

    return inner_fn


if __name__ == "__main__":

    class SingletonBaseClass(SingletonBase):
        pass

    class S1(SingletonBaseClass):
        pass

    class SingletonBaseMeta(metaclass=SingletonMeta):
        pass

    class S2(SingletonBaseMeta):
        pass

    # expected
    logger.info(SingletonBaseClass())  # same
    logger.info(SingletonBaseClass())  # same
    logger.info(S1())  # same

    # expected
    logger.info(SingletonBaseMeta())  # same
    logger.info(SingletonBaseMeta())  # same
    logger.info(S2())  # different
