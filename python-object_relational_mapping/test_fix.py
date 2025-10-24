#!/usr/bin/env python3
"""
Test script
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print("SCRIPT START")  # 👈 Premier print

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

print(f"Found {len(states)} states")  # 👈 Debug

for state in states:
    print(f"{state.id}: {state.name}")

session.close()
print("SCRIPT END")  # 👈 Dernier print
