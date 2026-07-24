#!/usr/bin/python3
"""Creates the ``states`` table in the database given on the CLI.

Using SQLAlchemy, the script builds an engine from the username,
password and database name arguments and calls
``Base.metadata.create_all`` so every model that inherits from ``Base``
(here, ``State``) gets its table created.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
