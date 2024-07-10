#!/usr/bin/python3
"""
Write a script that prints all city objects from the database
"""
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    Create a path to the database URL
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(State)
    
    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
