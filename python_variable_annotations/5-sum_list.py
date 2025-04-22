#!/usr/bin/env python3
''' Typed annotations sum_list'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''adding all float of the list'''
    return sum(input_list)
