#!/usr/bin/python3
""" This module test the rectangle class"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import io
import sys


class TestRectangle(unittest.TestCase):
    """This class defines the test class"""
    def test_inheritance(self):
        """This function checks the case for inheritance"""
        r1 = Rectangle(2, 5)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(isinstance(r1, Rectangle))

    def test_getter_setter(self):
        """This function checks getters and setters availability"""
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_validate_instantiation(self):
        """This function checks the instantiation"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "4", 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, "5")
        with self.assertRaises(ValueError):
            Rectangle(-1, 4, 3, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 4, 3, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, -1, 4, 3)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 5, 3)
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 5, -2, 9)
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 5, -1)

    def test_validate_setter(self):
        r1 = Rectangle(3, 5)
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(ValueError):
            r1.width = -5
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(ValueError):
            r1.height = -4
        with self.assertRaises(ValueError):
            r1.x = -5
        with self.assertRaises(ValueError):
            r1.y = -10

    def test_area(self):
        """This function checks the case for area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_display(self):
        """This function checks displayed output"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(2, 2)
        r1.display()
        output = captured_output.getvalue()
        self.assertIn("##\n##", output)

    def test_str(self):
        """This fucntion checks the modification of str"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        output = captured_output.getvalue()
        self.assertIn("[Rectangle] (12) 2/1 - 4/6", output)

    def test_update(self):
        """This function updates the attributes"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        print(r1)
        output = captured_output.getvalue()
        self.assertIn("[Rectangle] (89) 10/10 - 10/10", output)

    def test_save_to_file(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            print(file.read())
        output = captured_output.getvalue()
        self.assertIn('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]', output)
