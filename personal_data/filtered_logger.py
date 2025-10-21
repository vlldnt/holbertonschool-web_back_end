#!/Users/adrienv/Documents/Holberton/holbertonschool-web_back_end/personal_data/venv/bin/python
'''returns log message obfuscated'''


import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    '''Handles and returns a logger'''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Connection to a database and get data'''
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connection.MySQLConnection(
        user=user,
        password=password,
        host=host,
        database=db_name
    )


def main() -> None:
    """the main function"""
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users;")

    header = []
    for collumn in cur.description:
        header.append(collumn[0])

    logger = get_logger()

    for line in cur:
        info_answer = ''
        for field, para in zip(line, header):
            info_answer += f'{para}={field}; '
        logger.info(info_answer)

    cur.close()
    db.close()

if __name__ == '__main__':
    main()
