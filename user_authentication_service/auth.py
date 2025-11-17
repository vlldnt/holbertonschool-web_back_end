#!/usr/bin/env python3
'''Auth module for session'''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class with methods
    """

    def __init__(self):
        '''Init method self'''
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        '''Hashed password using bcrypt'''
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def register_user(self, email: str, password: str) -> User:
        """register a user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed = self._hash_password(password)
            return self._db.add_user(email, hashed)
