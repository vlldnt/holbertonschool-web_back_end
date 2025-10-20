#!/usr/bin/env python3
'''returns log message obfuscated'''


import re


def filter_datum(fields, redaction, message, separator):
    '''Change value by a new text format'''
    pattern = r'({})=([^{}]*)'.format('|'.join(fields), separator)
    return re.sub(pattern, lambda f: f"{f.group(1)}={redaction}", message)
