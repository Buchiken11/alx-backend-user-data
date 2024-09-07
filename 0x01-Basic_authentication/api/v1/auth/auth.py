#!/usr/bin/env python3
"This module contains the Auth class, which provides methods to handle
authorization and authentication logic for the API.
"""

from flask import Flask
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage authentication
    with public methods
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths
        will be used later
        Args:
            path- the route
            excluded_path - the routes that is not contained in path.
            Returns: False

        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        A public method to get the authorization
        from the request
        Args:
            request: Request to extract the header from
            Returns: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        A public method that retrieves the current user
        from the request
        Args:
            request:- the Flask request object 
            Returns:- None
        """
        return None
