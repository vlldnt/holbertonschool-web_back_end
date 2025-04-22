#!/usr/bin/env python3
'''make_multiplier / Callable'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Docntstring return function'''
    def mul_function(val: float) -> float:
        return multiplier * val
    return mul_function
