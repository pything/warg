#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = """
Generalised wrapper for delayed construction of class objects. Encapsulates kwargs and callable constructor with the option of modifying construction arguments before construction is finally performed.

"""

__all__ = ["GeneralisedDelayedKwargConstruction", "GDKC"]


import logging
from typing import Any, Callable, Mapping, MutableMapping, Sequence

logger = logging.getLogger(__name__)


class GeneralisedDelayedKwargConstruction:
    """
    A generalised class for setting up kwargs for later construction of an instance of an object
    [constructor, args, kwargs]
    """

    def __init__(self, constructor: Callable, *args: Any, **kwargs: Any):
        """
        [constructor, args, kwargs]

        :param constructor: The delayed callable, to be evaluated at __call__ or context __enter__
        :param args: arguments to use for evaluation, If only one is provided and is of typing mapping, it is assumed to be directly kwargs
        :param kwargs: arguments to use for evaluation
        """
        self.constructor: Callable = constructor
        assert len(args) < 2, f"Does not support multiple args, only a single mapping type"
        if len(args) == 1:
            assert isinstance(
                args[0], Mapping
            ), f"Arg[0] type is not a mapping type, was {type(args[0])} which is not supported"
        assert not (
            len(kwargs) > 0 and len(args) > 0
        ), f"Does not support both args and kwargs, both supplied args, {args} and {kwargs}"

        if len(args) == 1 and len(kwargs) == 0 and isinstance(args[0], Mapping):
            self.kwargs: MutableMapping = args[0]
        elif len(kwargs) == 1 and next(iter(kwargs.keys())) == "kwargs":
            self.kwargs = kwargs["kwargs"]
        else:
            self.kwargs: MutableMapping = kwargs

    def __enter__(self) -> Any:
        self.instance = self.__call__()
        return self.instance.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb) -> Any:
        return self.instance.__exit__(exc_type, exc_val, exc_tb)

    def __call__(self, *args, **kwargs) -> Any:
        """

        Allows last minute override of kwargs

        :param args:
        :param kwargs:
        :return:
        """

        war = "".join(
            [
                f"Overwriting {k} with the value {v} in construction of {self.constructor}"
                for (k, v), b in zip(kwargs.items(), self.kwargs.keys())
                if k == b
            ]
        )
        if war != "":
            logger.warning(war)

        self.kwargs.update(kwargs)
        try:
            return self.constructor(*args, **self.kwargs)
        except TypeError as e:
            e.args += (f"in construction of {self.constructor}",)
            raise e


GDKC = GeneralisedDelayedKwargConstruction

if __name__ == "__main__":

    class UnreachableError(Exception):
        pass

    class A:
        """description"""

        def __init__(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]):
            pass

    def stest_not_both() -> None:
        """
        :rtype: None
        """
        GeneralisedDelayedKwargConstruction(A, [1], a=2)

    def stest_kw() -> None:
        """
        :rtype: None
        """
        GeneralisedDelayedKwargConstruction(A, a=2)

    def stest_mapping() -> None:
        """
        :rtype: None
        """
        GeneralisedDelayedKwargConstruction(A, {"a": 2})

    def stest_mapping_and_args_fail() -> None:
        """
        :rtype: None
        """
        GeneralisedDelayedKwargConstruction(A, {"a": 2}, 1)

    def stest_mapping_and_args_fail_inv() -> None:
        """
        :rtype: None
        """
        GeneralisedDelayedKwargConstruction(A, 1, {"a": 2})

    stest_kw()
    stest_mapping()

    try:
        stest_mapping()  # Successful
        raise UnreachableError
    except UnreachableError:  # Is expected
        pass
    try:
        stest_mapping_and_args_fail()
        raise UnreachableError
    except AssertionError:
        pass
    try:
        stest_mapping_and_args_fail_inv()
        raise UnreachableError
    except AssertionError:
        pass
    try:
        stest_not_both()
        raise UnreachableError
    except AssertionError:
        pass
