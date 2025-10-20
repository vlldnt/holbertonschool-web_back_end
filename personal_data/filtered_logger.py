#!/usr/bin/env python3
'''returns log message obfuscated'''


import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Change value by a new text format'''
    for field in fields:
        message = re.sub(f"{field}=(.*?){separator}",
                         f"{field}={redaction}{separator}",
                         f"{message}")
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        '''get message and return the formated message'''
        message = record.getMessage()
        record.msg = filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)
        return super().format(record)
