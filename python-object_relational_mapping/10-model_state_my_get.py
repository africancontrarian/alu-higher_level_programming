#!/usr/bin/python3
"""Prints the id of the State whose name is given as an argument.

The name is passed to the ORM ``filter`` as a bound value, so the query
is safe from SQL injection. The state's ``id`` is printed, or
``Not found`` when no state matches.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(
        State.name == sys.argv[4]).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
    session.close()
