#!/usr/bin/python3
"""
Display all City objects with their State
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    session = Session(engine)
    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()
    
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()