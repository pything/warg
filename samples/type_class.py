class A: ...


import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(type(A))
