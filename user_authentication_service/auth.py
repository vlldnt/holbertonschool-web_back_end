#!/usr/bin/env python3
'''Auth module for session'''

import bcrypt


def _hash_password(password: str) -> bytes:
    '''Hashed password using bcrypt'''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
