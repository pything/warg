__all__ = ["add_logging_handler_once", "SinkWriter"]

import logging
from typing import Any

_logger = logging.getLogger(__name__)


def add_logging_handler_once(_logger: logging.Logger, handler: object) -> bool:
    """A helper to add a handler to a logger, ensuring there are no duplicates.

    :param _logger: Logger that should have a handler added.
    :type _logger: logging.logger

    :param handler: Handler instance to be added. It will not be added if an
        instance of that Handler subclass already exists.
    :type handler: logging.Handler

    :returns: True if the logging handler was added, otherwise False.
    :rtype: bool
    """
    class_name = handler.__class__.__name__
    for handler in _logger.handlers:
        if handler.__class__.__name__ == class_name:
            return False

    _logger.addHandler(handler)
    return True


class SinkWriter:

    def write(self, text: Any) -> None:
        pass
