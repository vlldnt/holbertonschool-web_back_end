#!/usr/bin/env python3
''' Type annoted sum_mixed_list'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Documentation mixed sum list'''
    return float(sum(mxd_lst))
