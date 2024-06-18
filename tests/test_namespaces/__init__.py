import logging

import ok_namespace

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(ok_namespace.__all__)
    logger.info(dir(ok_namespace))
    logger.info(ok_namespace.func2())
    logger.info(ok_namespace.func1())
