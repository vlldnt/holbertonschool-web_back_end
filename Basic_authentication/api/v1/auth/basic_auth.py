#!/usr/bin/env python3
"""
Basic Authentication module for the API.

This module provides the base Auth class that handles authentication
for the API endpoints.
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''Basic Auth inherit form Auth'''
    pass
