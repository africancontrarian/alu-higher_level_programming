#!/usr/bin/python3
"""Defines the State model with a relationship to its cities.

In addition to the plain ``State`` mapping, this version exposes a
``cities`` relationship that cascades deletions: removing a ``State``
also removes every ``City`` linked to it. The reverse reference from a
``City`` to its owner is named ``state``.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a US state and the cities that belong to it."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade="all, delete, delete-orphan")
