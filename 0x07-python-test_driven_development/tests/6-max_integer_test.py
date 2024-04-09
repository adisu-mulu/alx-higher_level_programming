#!/usr/bin/python3
"""
This module is used for unit testing of a function that retrieves the max integer of a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
The class TestMaxInteger extends the TestCase class of unittest module
"""
    
    def test_list(self):
        """The function test_list test used to perform various test cases on the the function max_integer
        """
        self.assertAlmostEqual(max_integer([]), None)
