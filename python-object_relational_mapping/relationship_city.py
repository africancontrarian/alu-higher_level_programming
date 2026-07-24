#!/usr/bin/python3
"""Defines the City model used with the relationship-based State.

The ``City`` class reuses the declarative ``Base`` from
``relationship_state`` and links to the ``states`` table through a
foreign key; the ``state`` back reference is provided by the ``State``
relationship.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Represents a city that belongs to a single state."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
