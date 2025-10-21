#!/usr/bin/env python3
'''Encrypt password with bcrypt'''


import bcrypt


def hash_password(password: str) -> str:
    '''encrypt password with bcrypt'''

    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return (hash)
