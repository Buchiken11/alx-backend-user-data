#!/usr/bin/env python3

import bcrypt


def hash_password(password: str) -> bytes:
    '''
    hashed passaord with bcrypt
    
    Returns:
    salted hashed password
    '''
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    is_valid function returns a boolen
    Arguement:

    hashed_password: the password to check against
    
    password: plain text to be hashed
    '''

    return bcrypt.checkpw(password.encode(), hashed_password)
