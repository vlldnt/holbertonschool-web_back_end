#!/usr/bin/env python3
"""
Session Authentication module for the API.

This module provides the base Auth class that handles authentication
for the API endpoints.
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    'Session Auth inherit from Auth'

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        'Creation of a session'

        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
