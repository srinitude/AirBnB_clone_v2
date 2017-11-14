#!/usr/bin/python3
"""
Contains the DBStorage class
"""
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}

class DBStorage:
    """ """
    __engine == None
    __session == None

    def __init__(self):
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

        user = environ.get['HBNB_MYSQL_USER']
        pwd = environ.get['HBNB_MYSQL_PWD']
        host = environ.get['HBNB_MYSQL_HOST']
        db = environ.get['HBNB_MYSQL_DB']
        port = 3306

        if environ.get['HBNB_ENV'] == 'test':
               Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=some_engine)
        self.__session = Session()


    def all(self, cls=None)::
        """ """
        if cls == None:
            #query all types of objects:
            #(User, State, City, Amenity, Place and Review)

        # must return a dictionary: (like FileStorage)
            # key = <class-name>.<object-id>
            # value = object


    def new(self, obj):
        """ Adds object to the current database session"""
        self.__session.add(obj)


    def save(self):
        """ Commits all changes of the current database session"""
        self.__session.commit()


    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj not None:
               self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit = false)
        Session = scoped_session(session_factory)
