#!/usr/bin/env python3
'''returns log message obfuscated'''


import re
from typing import List


def filter_datum(fields: List[str], redaction: str, 
                 message: str, separator: str) -> str:
    '''Change value by a new text format'''
    pattern = r'({})=([^{}]*)'.format('|'.join(fields), separator)
    return re.sub(pattern, lambda f: f"{f.group(1)}={redaction}", message)
