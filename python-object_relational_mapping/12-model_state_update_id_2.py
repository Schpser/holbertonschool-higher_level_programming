#!/usr/bin/python3
"""
Update a state
"""
import sys
from model_state import Base, State
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

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    print(state.id)

    session.close()
