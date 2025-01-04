#!/usr/bin/python3
""" """
import unittest
from models.city import City
from time import sleep
import datetime
import os


class test_City(unittest.TestCase):
    """ """

    def test_two_cities_created_at(self):
        """"""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_two_cities_different_updated_at(self):
        """"""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        """Test the string City."""
        dt = datetime.today()
        dt_repr = repr(dt)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        city_str = city.__str__()
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': " + dt_repr, city_str)
        self.assertIn("'updated_at': " + dt_repr, city_str)

    def test_args_unused(self):
        """"""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_None_kwargs(self):
        """"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySave(unittest.TestCase):
    """"""

    @classmethod
    def setUpClass(cls):
        """"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """"""
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)
