#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User, Base
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str)-> User:
        '''
        defines an add_user method
        Args:
            email: user email to be added
            hashed_password: the hashed password from bcrypt
            on the users password
            Returns: the added new user
        '''
        session = self._session
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            session.add(new_user)
            session.commit()
        except Exception:
            session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        '''
        Db.find_user_by method that returns the first
        row found in users

        Args:
            first_user: Arbitrary argument to filter users
        Returns: user the first match in user row

        Raises: NoResultFound: if no result are found
                InvalidRequestError: if wrong query aguments are found
        '''
        attrs, vals = [], []
        for attr, val in kwargs.items():
            if not hasattr(User, attr):
                raise InvalidRequestError()
            attrs.append(getattr(User, attr))
            vals.append(val)
        session = self._session
        query = session.query(User)
        user = query.filter(tuple_(*attrs).in_([tuple(vals)])).first()
        if not user:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        '''
        A method to updqte the DB

        Args: 
            user_id (type int) of the user's id

        Returns:
             None

        Raises:

            ValueError if the agument passed is not the one passed by the user
        '''

        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"User has no attribute '{key}'")

            setattr(user, key, value)
        self._session.commit()
