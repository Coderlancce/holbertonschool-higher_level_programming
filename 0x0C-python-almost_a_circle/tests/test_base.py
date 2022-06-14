#!/usr/bin/python3
""" Module for test Base class """
import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.base import Base

class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def testId(self):
        """ Test assigned id """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def testIdDefault(self):
        """ Test assigned more id """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def testIdMix(self):
        """ Test assigned number id and empty id """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def testIdString(self):
        """ Test assigned string number """
        b1 = Base("1")
        self.assertEqual(b1.id, "1")

    def testIdTwoArgs(self):
        """ Test assigned two arguments """
        with self.assertRaises(TypeError):
            b1 = Base(1, 1)
        
