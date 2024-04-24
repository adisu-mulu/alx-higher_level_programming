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
