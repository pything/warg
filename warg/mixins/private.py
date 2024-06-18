#!/usr/bin/env python3

__author__ = "heider"
__doc__ = r"""

           Created on 9/9/22
           """

__all__ = ["PrivateAttributeMixin"]

import logging
from typing import Any

logger = logging.getLogger(__name__)


class PrivateAttributeMixin:
    def __getitem__(self, key: str) -> Any:
        if key.startswith("_"):
            return None
        return getattr(self, key, None)
