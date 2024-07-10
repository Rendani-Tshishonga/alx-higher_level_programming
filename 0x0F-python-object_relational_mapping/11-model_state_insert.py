#!/usr/bin/python3
"""
Write a script that adds the State object "Louisiana" to the database
hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    We will connect to the database using a URL
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(database_url)

    Session = sessionmaker(bind=engine)

    session = Session()
    
    """
    We will create add a state name "Louisiana" to the database
    """
    state_add = State(name="Louisiana")
    session.add(state_add)
    
    """
    We will be required to persist the changes to the database through the commit function
    """
    session.commit()

    """
    We will return the updated results which have been commited by 
    retutning the state.id of the newly added state name
    """
    print("{}".format(state_add.id))
    session.close()

