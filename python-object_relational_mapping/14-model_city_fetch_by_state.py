#!/usr/bin/python3
"""Lists all City objects together with their state name.

The ``cities`` and ``states`` tables are joined through the ORM and the
result is printed as ``<state name>: (<city id>) <city name>`` sorted by
``cities.id``.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
