#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    Create a path to the database object using a URL
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    tables = session.query(State).filter(State.name.contains('a'))

    """
    tables will return a tuple of state names which contain the letter
    "a" in them and we will iteratively access the tuple to return the 
    states we woould need to delete from the table
    """
    
    for table in tables:
        session.delete(table)

    session.commit()

    session.close()
