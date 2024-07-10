#!/usr/bin/python3
"""
Write a script that prints the state.id of the State object with the name passed as argument 
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    Connect to a database using a URL
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    """
    We will run a query that will return the state.id else we will return not found 
    if no argument has been passed to the command line
    """
    session = Session()
    tables = session.query(State).filter(State.name == sys.argv[4]).first()
    
    if tables is None:
        print("Not found")
    else:
        print("{}".format(tables.id))
