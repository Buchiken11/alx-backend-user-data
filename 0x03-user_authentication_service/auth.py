#!/usr/bin/env python3
'''
Authentication module
'''
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers new user
            Args:
                - email: user's email
                - password: user's password
            Return:
                - User 
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user
        else:
            raise ValueError(f"User {email} already exists")

def _hash_password(password: str) -> bytes:
    '''
    a method for generating hashed password using bcrypt
    Args:
        
        Password: the original user's password to be hashed

        Returns:
            the salted hash of the password
    '''
    if password is None:
        return None
        
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode('utf-8'), salt)


def valid_login(self, email: str, password: str) -> bool:
    ''' 
    Endpoint to Checks if password is valid
    Args:
    - email: user's email
    - password: user's password
    Returns:
        True if credentials are valid, otherwise False
    '''
    db = self._db
    try:
        user = db.find_user_by(email=email)
    except NoResultFound:
        return False
    if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
        return False
    return True

def _generate_uuid() -> str:
    '''Generates unique ids
        Return:
            - UUID generated
    '''
    return str(uuid4())
