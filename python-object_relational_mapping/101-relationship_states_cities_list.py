#!/usr/bin/python3
"""Lists all State objects with their cities using the relationship.

A single query loads every ``State`` (ordered by ``id``); the linked
cities are read through the ``cities`` relationship and printed,
indented with a tabulation, sorted by ``cities.id``.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda c: c.id):
            print("\t{}: {}".format(city.id, city.name))
    session.close()
