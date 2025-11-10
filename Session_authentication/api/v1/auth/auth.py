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
        '''Check if needed auth for a given path'''

        if path is None or excluded_paths is None:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        '''authorization header method'''

        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''method for return current user'''
        return None
