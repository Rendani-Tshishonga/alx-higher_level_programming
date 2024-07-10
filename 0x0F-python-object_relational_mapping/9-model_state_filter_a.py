#!/usr/bin/python3
"""
Write a script that lists all State objects that contain the letter a from the 
database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    
    tables = session.query(State).filter(State.name.contains('a'))

    for table in tables:
        print("{}: {}".format(table.id, table.name))
    

