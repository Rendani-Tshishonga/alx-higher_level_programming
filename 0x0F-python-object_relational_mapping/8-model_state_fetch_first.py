#!/usr/bin/python3
"""
Write a script that prints the first State object from the database 
hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    Connect to the database uisng a url or a path to your database
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    table = session.query(States).order_by(states.id).first()

    if table is None:
        print("Nothing")
    else:
        print("{}: {}".format(table.id, table.name))
