#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:
    '''
    an auth class with public methods
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        def require(): public method, eg it can be accessed outside the class
        Args:
            path: the paths to be checked
            excluded_paths: paths to be excluded
        '''
        if path == None:
            return True
        if excluded_paths == None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
            for excluded_path in excluded_paths:
                if not excluded_path.endswith('/') or excluded_path == path:
                    return True
                return False

    def authorization_header(self, request=None) -> str:
        '''
        def authorized_header(): public method
        Returns: None
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        def current_user(): public method
        Returns: None
        '''
        return None
