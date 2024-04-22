#!/usr/bin/python3
""" This module is used to test the base class"""
from models.base import Base

import unittest


class TestBase(unittest.TestCase):
    """ This class defines the base test class"""
    def test_id_not_None(self):
        """this function test wether id is not none"""
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_id_none(self):
        """This function test the case where id is none"""
        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        self.assertEqual(b2.id, Base._Base__nb_objects)
