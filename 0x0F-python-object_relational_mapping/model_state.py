#!/usr/bin/python3
"""
Write a pythonn script that contains the class definition of a state
and an instance Base = declaritive_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""
The declarative system are defined in terms of a base class 
which maintains a catalog of classes and tables relative
to that base. This is known as the declarative base class.
"""
Base = declarative_base()

"""
We will define a class States which will be mapped to the states table
We will use the __table__ attribute for the table name
the id attribute for a auto-incremented id field
and a name attribute which will be uses to store the name of the state
"""
class State(Base):
    __tablename__ = 'states'

    id = Column(Interger, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
