#!/usr/bin/python3
""" Module test renctangle class """
import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle Class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def testCallFather(self):
        """ test for count empty call to father class to chech id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def testCallFatherComplete(self):
        """ test complete send arguments father for check id """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def testErrorOneArgument(self):
        """ test if the input is one argument """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def testErrorTypeStrings(self):
        """ test if some element is a string """
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, "10", 5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 2, 3, "4")

    def testErrorTypeFloat(self):
        """ test if some element is a float """
        with self.assertRaises(TypeError):
            r2 = Rectangle(10.3, 4)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10 , 4.1)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 4, 3.1)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 4, 3, 2.1)

    def testErrorValue(self):
        """ test if some element is negative """
        with self.assertRaises(ValueError):
            r2 = Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -2)
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, -2, 3)
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 2, 3, -4)

    def testErrorZero(self):
        """ test if dimensions is zero """
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 0)

    def testArea(self):
        """ test area """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def testDisplay(self):
        """ test display """
        r1 = Rectangle(4, 6)
        res = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def testDisplayTwo(self):
        """ Test display """
        r2 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r2.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str_(self):
        """ test __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_a(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_b(self):
        """ Test __str__ return value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_c(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def testDisplayAdvanced(self):
        """ Test new requirments of display """
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def testDisplayAdvancedA(self):
        """ test new requirments of display """
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def testUpdateA(self):
        """ test update args """
        r1 = Rectangle(10, 10, 10, 10)
        res = "[Rectangle] (1) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        resA = "[Rectangle] (89) 10/10 - 10/10\n"
        r1.update(89)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), resA)

        resB = "[Rectangle] (89) 10/10 - 2/10\n"
        r1.update(89, 2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), resB)

    def testUpdateAdvanced(self):
        """ test update kwargs """
        r1 = Rectangle(10, 10, 10, 10)
        res = "[Rectangle] (1) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        resA = "[Rectangle] (1) 10/10 - 10/1\n"
        r1.update(height=1)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), resA)

        resB = "[Rectangle] (1) 2/10 - 1/1\n"
        r1.update(width=1, x=2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), resB)
