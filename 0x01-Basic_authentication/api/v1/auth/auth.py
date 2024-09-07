#!/usr/bin/env python3
"""
This module contains the Auth class, which provides methods to handle
authorization and authentication logic for the API.
"""

from flask import Flask
from typing import List, TypeVar
# import fnmatch


class Auth:
    """
    Auth class to manage authentication with public methods
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False - path and excluded_paths will be used later
        Args:
            path: The route
            excluded_paths: The routes that are not contained in path.
        Returns:
            bool: False
        """
        if path and not path.endswith('/'):
            path = path + '/'  # path = path + '/'

        if not path or path not in excluded_paths:

            return True

        if not excluded_paths or excluded_paths == []:

            return True

        if path in excluded_paths:

            return False

    def authorization_header(self, request=None) -> str:
        """
        A public method to get the authorization header from the request.

        Args:
            request: Request to extract the header from.
        Returns:
            str: The authorization header or None if not present.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        A public method that retrieves the current user from the request.
        Args:
            request: The Flask request object.
        Returns:
            User: The current user or None if not present.
        """
        return None
