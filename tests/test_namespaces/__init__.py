import logging

import ok_namespace

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    _logger.info(ok_namespace.__all__)
    _logger.info(dir(ok_namespace))
    _logger.info(ok_namespace.func2())
    _logger.info(ok_namespace.func1())
