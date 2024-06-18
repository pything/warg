#!/usr/bin/env python3
from typing import Any, MutableMapping, Sequence

from warg import drop_unused_kws
from warg.metas.post_init import PostInit

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""
           """


import logging

logger = logging.getLogger(__name__)


def test_post_init_class():
    class MyTestingClass(metaclass=PostInit):
        """
        class with the metaclass passed as an argument"""

        @drop_unused_kws
        def __init__(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
            logger.info(kwargs)

        def __post_init__(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
            logger.info(args, kwargs)

        def __call__(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
            logger.info("a")

    a = MyTestingClass("asdc", kas=2)

    a()


def test_post_init_no_kws_class():
    class MyTestingClass(metaclass=PostInit):
        """
        class with the metaclass passed as an argument"""

        @drop_unused_kws
        def __init__(self, *args: Sequence):
            logger.info("Init class")

        @drop_unused_kws
        def __post_init__(self, *args: Sequence):
            logger.info(args)

        def __call__(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
            logger.info("a")

    a = MyTestingClass("asdc", kas=2)

    a()


def test_no_post_init_class():
    class MyTestingClass(metaclass=PostInit):
        """
        class with the metaclass passed as an argument"""

        def __init__(self):
            logger.info("Init class")

        def __call__(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
            logger.info("a")

    a = MyTestingClass()

    a()
