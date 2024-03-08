#!/usr/bin/python3
""" DB Storage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """ This class manages storage of hbnb models in MySQL """

    __engine = None
    __session = None

    def __init__(self):
        """ Creates the engine, session, and drops tables if in test mode """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries all objects in the current session """

        from models import classes

        objects = {}
        if cls:
            query_result = self.__session.query(classes[cls]).all()
        else:
            for cls in classes.values():
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj

        return objects

    def new(self, obj):
        """ Adds the object to the current session """
        if obj not in self.__session:
            self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current session """
        try:
            self.__session.commit()
        except Exception as e:
            print(e)
            self.__session.rollback()

    def delete(self, obj=None):
        """ Deletes obj from the current session if not None """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Creates all tables in the database and creates a session """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ Close session."""
        self.__session.close()
