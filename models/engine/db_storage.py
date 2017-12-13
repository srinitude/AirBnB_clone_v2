#!/usr/bin/python3
"""
Contains the DBStorage class
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.exc import InvalidRequestError

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """ """
    __engine = None
    __session = None
    __scoped_session = None
    __objects = {}

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        port = 3306

        dev = ('mysql+mysqldb://{}:{}@{}:{}/{}'.format(user,
                                                       pwd,
                                                       host,
                                                       port,
                                                       db))

        self.__engine = create_engine(dev)

# self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format
        #                               (user,
        #                                pwd,
        #                                host,
        #                                port,
        #                                db)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Gets all the objects"""
        self.__objects.clear()
        if not cls:
            for key, value in classes.items():
                try:
                    objects = self.__session.query(value).all()
                    for obj in objects:
                        obj_key = obj.__class__.__name__ + "." + obj.id
                        self.__objects[obj_key] = obj
                except InvalidRequestError:
                    pass
            return self.__objects
        else:
            cls = classes[cls]
            objects = self.__session.query(cls).all()
            for obj in objects:
                obj_key = obj.__class__.__name__ + "." + obj.id
                self.__objects[obj_key] = obj
            return self.__objects

    def new(self, obj):
        """ Adds object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__scoped_session = Session
        self.__session = Session()

    def close(self):
        """Closes DB Storage"""
        self.__scoped_session.remove()
        self.reload()
