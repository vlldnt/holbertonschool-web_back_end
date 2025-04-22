#!/usr/bin/env python3
'''Annotate the fucntion'''


from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Annotate the given function for exercice'''
    return [(i, len(i)) for i in lst]
