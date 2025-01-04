#!/usr/bin/python3
""" """

from models.amenity import Amenity
import unittest
import datetime
import models
from time import sleep


class test_Amenity(unittest.TestCase):
    """Test cases for Amenity instantiation."""

    def test_no_args_instantiates(self):
        """"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_in_objects(self):
        """"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """"""
        self.assertEqual(datetime.datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """"""
        self.assertEqual(datetime.datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """"""
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        """"""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        """"""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        """"""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)
