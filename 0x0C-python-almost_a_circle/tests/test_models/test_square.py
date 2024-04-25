#!/usr/bin/python3
"""This module defines test cases for the Square class"""
from models.rectangle import Rectangle
from models.square import Square
import unittest
import io
import sys


class TestSquare(unittest.TestCase):
    """This class defines the test class"""
    def test_inheritance(self):
        """This function checks the case for inheritance"""
        s1 = Square(5)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(isinstance(s1, Square))

    def test_str(self):
        """This fucntion checks the modification of str"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s1 = Square(5)
        print(s1)
        output = captured_output.getvalue()
        self.assertIn("[Square] (2) 0/0 - 5", output)

    def test_update(self):
        """This function test the cases for updation"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s1 = Square(5)
        s1.update(10)
        s1.update(1, 2)
        s1.update(1, 2, 3)
        s1.update(1, 2, 3, 4)
        s1.update(x=12)
        s1.update(size=7, y=1)
        s1.update(size=7, id=89, y=1)
        print(s1)
        output = captured_output.getvalue()
        self.assertIn("[Square] (89) 12/1 - 7", output)

    def test_to_dictioary(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        print(type(s1_dictionary))
        output = captured_output.getvalue()
        self.assertIn("<class 'dict'>", output)
