#!/usr/bin/python3
"""
Write a script that changes the name of the State object from the database
hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    We will create a path to our database through a URL
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    table = session.query(State).filter(State.id == 2).first()
    table.name = "New Mexico"
    session.commit()

    session.close()
