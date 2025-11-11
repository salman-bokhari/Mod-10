import logging
from typing import Union

logger = logging.getLogger(__name__)

def add(a: Union[int,float], b: Union[int,float]) -> float:
    logger.debug("Adding %s + %s", a, b)
    return a + b

def sub(a: Union[int,float], b: Union[int,float]) -> float:
    logger.debug("Subtracting %s - %s", a, b)
    return a - b

def mul(a: Union[int,float], b: Union[int,float]) -> float:
    logger.debug("Multiplying %s * %s", a, b)
    return a * b

def div(a: Union[int,float], b: Union[int,float]) -> float:
    logger.debug("Dividing %s / %s", a, b)
    if b == 0:
        logger.error("Division by zero attempted: %s / %s", a, b)
        raise ZeroDivisionError("Division by zero")
    return a / b
