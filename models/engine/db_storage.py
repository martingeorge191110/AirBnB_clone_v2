#!/usr/bin/python3
"""DB Storage file"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """retrieve env"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                           user, password, host, database),
                           pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for class_type in ["State", "City", "User", "Place", "Review"]:
                objects.extend(self.__session.query(class_type).all())

            return {f"{type(obj).__name__}.{obj.id}": obj for obj in objects}

    def new(self, obj): 
        """add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self): 
        """commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Setting up all tables in the database"""
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
