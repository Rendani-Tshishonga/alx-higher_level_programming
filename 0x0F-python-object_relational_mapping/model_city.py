#!/usr/bin/python3
"""
Write a python file that contains a class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
