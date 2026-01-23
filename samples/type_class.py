class A: ...


import logging

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    _logger.info(type(A))
