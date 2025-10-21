#!/usr/bin/env python3
'''Encrypt password with bcrypt'''


import bcrypt


def hash_password(password: str) -> bytes:
    '''encrypt password with bcrypt'''
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return (hash)


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Check the validity of a password'''
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed_password)
