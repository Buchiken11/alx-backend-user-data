#!/usr/bin/env pythone

from flask import Flask
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage authentication
    Purpose: This class is the template for all
        authentication system you will implement.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths
        will be used later
        now, you don’t need to take care of them
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        that returns None - request will be the
        Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        that returns None - request will be
        the Flask request object
        """
        return None
