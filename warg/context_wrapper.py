#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 01/07/2020
           """

__all__ = ["ContextWrapper", "NopContext"]

import contextlib
import inspect
import logging
from typing import Callable, ContextManager, Mapping, Optional, Sequence

logger = logging.getLogger(__name__)


class NopContext(contextlib.AbstractContextManager):
    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        return


class ContextWrapper(contextlib.AbstractContextManager):
    """
    Allows for conditional application of contexts, if uninstantiated context manager classes are passed no arguments
    is supplied in construction.
    if disabled, None is returned if enabled return of context manager is propagated"""

    def __init__(
        self,
        context_manager: ContextManager,
        enabled: bool,
        construction_args: Sequence = (),
        construction_kwargs: Optional[Mapping] = None,
    ):
        if construction_kwargs is None:
            construction_kwargs = {}

        self._context_manager = context_manager
        self._enabled = enabled
        self._construction_args = construction_args
        self._construction_kwargs = construction_kwargs

    def __enter__(self):
        if self._enabled:
            if inspect.isclass(self._context_manager) or isinstance(self._context_manager, Callable):
                self._context_manager = self._context_manager(
                    *self._construction_args, **self._construction_kwargs
                )
            if hasattr(self._context_manager, "__enter__"):
                return self._context_manager.__enter__()
            else:
                raise NotImplementedError(f"{self._context_manager} does not implement __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._enabled:
            return self._context_manager.__exit__(exc_type, exc_val, exc_tb)


if __name__ == "__main__":

    class SampleContextManager(contextlib.AbstractContextManager):
        """description"""

        def __init__(self, message="Hello World"):
            self._message = message

        def __enter__(self):
            logger.info(self._message)

        def __exit__(self, exc_type, exc_val, exc_tb):
            logger.info(not self._message)  # False ;)

    def main() -> None:
        """
        :rtype: None
        """
        with ContextWrapper(SampleContextManager, True):
            logger.info("with enabled")

        logger.info()
        with ContextWrapper(SampleContextManager, False):
            logger.info("with disabled")

        logger.info()
        with ContextWrapper(SampleContextManager, True):
            logger.info("with enabled, uninstantiated")

    main()
