#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    """DBStorage relationship"""
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete, delete-orphan"
    )

    """FileStorage relationship"""
    @property
    def cities(self):
        """Getter attribute to return the list of City instances"""
        from models import storage
        from models.city import City

        all_cities = storage.all(City)

        return [
            city for city in all_cities.values()
            if city.state_id == self.id
            ]
