#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """class State"""
    __tablename__ = 'states'

    name = Column(
        String(128),
        nullable=False)

    data = getenv("HBNB_TYPE_STORAGE")

    if (data == "db"):
        cities = relationship('City', backref="state", cascade="all, delete")

    if data != 'db':
        @property
        def cities(self):
            """Method that returns a list of cities depends on the given id."""
            cities = []
            all_cities = models.storage.all(City)
            for city_obj in all_cities.values():
                if city_obj.state_id == self.id:
                    cities.append(city_obj)
            return cities
