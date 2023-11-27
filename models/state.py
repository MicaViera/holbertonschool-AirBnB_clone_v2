#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    
    name = Column(
        String(128),
        nullable=False
    )
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', 
            backref="state",
            cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Method that returns the list of City instances."""
        city_list = []
        for key, value in storage._FileStorage__objects.items():
            key = key.split(".")
            if key == 'City' and value.state_id == self.id:
                city_list.append(value)
        return city_list
