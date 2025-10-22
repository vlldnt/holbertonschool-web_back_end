from flask import request  # type:ignore
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
        return None
