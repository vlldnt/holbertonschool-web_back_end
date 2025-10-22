#!/usr/bin/env python3
"""
Authentication module for the API.

This module provides the base Auth class that handles authentication
for the API endpoints.
"""

from flask import request
from typing import List, TypeVar


class Auth():
    '''Authentification class'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require auth method'''
        return False

    def authorization_header(self, request=None) -> str:
        '''authorization header method'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''method for return current user'''
        return None
