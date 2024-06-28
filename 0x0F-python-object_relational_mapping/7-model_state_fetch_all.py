#!/usr.bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa

"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """
    Access the database through a url or a path to the database 
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(database_url)

    """
    We will start communicating to the database using the session
    The Session will serve as a factory for all new session objects
    which will be bound to our database
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Below we will indicate a query which loads state instances which will be created
    on a session which we have instantiated above
    """
    for instance in session.query(State).order_by(states.id):
        print("{}: {}".format(instance.id, instance.name))

