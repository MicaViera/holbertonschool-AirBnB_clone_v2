#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreignkey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    
    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        String(60),
        nullable=False,
        ForeignKey('states.id'),
    )
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place', backref="cities",
                              cascade="all, delete, delete-orphan")
