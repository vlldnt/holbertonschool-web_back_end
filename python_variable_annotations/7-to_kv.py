#!/usr/bin/env python3
'''To KV function'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Docstring for the function'''
    return (k, float(v ** 2))
