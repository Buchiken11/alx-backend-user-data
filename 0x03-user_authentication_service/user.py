#!/usr/bin/env python3
'''
A mapping declaration of SQLACHEMY
'''
import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):

    '''
    A database model that inherits from Base
    '''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                self.name, self.fullname, self.nickname)
