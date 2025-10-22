#!/usr/bin/env python3
"""
Basic Authentication module for the API.

This module provides the base Auth class that handles authentication
for the API endpoints.
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    '''Basic Auth inherit form Auth'''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Extract and return a Base64 part of
        Authorization header for a basic auth'''

        if (authorization_header is None
            or not isinstance(authorization_header, str)
                or not authorization_header.startswith('Basic ')):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        '''Returning the decoded value of a Base64 string'''

        if (base64_authorization_header is None
                or not isinstance(base64_authorization_header, str)):
            return None

        try:
            b64decode = base64.b64decode(base64_authorization_header)
            utf8decode = b64decode.decode('utf-8')
            return utf8decode

        except Exception:
            return None
