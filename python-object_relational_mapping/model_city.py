#!/usr/bin/python3
"""Defines the City model mapped to the ``cities`` MySQL table.

The ``City`` class reuses the declarative ``Base`` from ``model_state``
and links back to the ``states`` table through a foreign key.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city stored in the ``cities`` table."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
