#!/usr/bin/python3

"""
    This module Contains The Test Cases for ```6-max_integer.py```
"""

import unittest
max_integer = __import__('6-max_integer').max_integer 

class TestCase(unittest.TestCase):
    """
    This Class Contains The different Test Cases for the Module above
    """

    def test_moduleDoc(self):
        """ Test Case for Module Documentation"""

        mod = __import__('6-max_integer').__doc__
        mod_t = len(mod) > 1
        self.assertTrue(mod_t)
        
    def test_functionDoc(self):
        """ Test Case for Function Documentation"""

        mod_t = len(max_integer.__doc__) > 1
        self.assertTrue(mod_t)

    def test_positiveNumbers(self):
        """ Test Cases for Positive Numbers """

        self.assertEqual(max_integer([9, 10, 99]), 99)
        self.assertEqual(max_integer([99, 10, 88]), 99)

    def test_negativeNumbers(self):
        """ Test Cases for Negative Numbers """

        self.assertEqual(max_integer([-1, -2, 0, -1]), 0)
        self.assertEqual(max_integer([-9, -8, 9, 0, -99]), 9)
