#!/usr/bin/python3
"""The new engine DBStorage."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """db Storage engine."""
    __engine = None
    __session = None

    def __init__(self):
        """Method that initializes the class."""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects."""
        dictionary = {}
        if cls is None:
            objects = self.__session.query().all()
        else:
            objects = self.__session.query(cls).all()
        for obj in objects:
            dictionary[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return dictionary
    
    def new(self, obj):
        """Method that adds to the current database session."""
        self.__session.add(obj)

    def save(self, obj=None):
        """Method that commits all the changes to the current database sesion"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method that deletes obj from the current database session."""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """Method that creates all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_creation = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_creation)
        self.__session = Session()
