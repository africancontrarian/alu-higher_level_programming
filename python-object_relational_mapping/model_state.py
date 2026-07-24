#!/usr/bin/python3
"""Defines the State model mapped to the ``states`` MySQL table.

The module exposes the SQLAlchemy declarative ``Base`` and the ``State``
class so other scripts can create the table and query it through the
ORM instead of writing raw SQL.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a US state stored in the ``states`` table."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
