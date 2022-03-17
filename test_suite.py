#! usr/bin/python3

import unittest
from fractions import fraction as fh

class TestFractionExpressions(unittest.TestCase):
    
    def test_addition(self):
        a = fh(1, 2)
        b = fh(1, 3)
        actual = a + b
        expected = fh(5, 6)
        self.assertEqual(str(actual), str(expected), 'Expected sum of two fractions.')
        actual = a + a
        expected = fh(1, 1)
        self.assertEqual(str(actual), str(expected), 'Expected reduced form of fraction.')
    
    def test_subtraction(self):
        a = fh(1, 2)
        b = fh(1, 3)
        actual = a - b
        expected = fh(1, 6)
        self.assertEqual(str(actual), str(expected), 'Expected difference of two fractions.')
    
    def test_multiplication(self):
        a = fh(1, 2)
        b = fh(1, 3)
        actual = a * b
        expected = fh(1, 6)
        self.assertEqual(str(actual), str(expected), 'Expected product of two fractions.')
    
    def test_division(self):
        a = fh(1, 2)
        b = fh(1, 3)
        actual = a / b
        expected = fh(3, 2)
        self.assertEqual(str(actual), str(expected), 'Expected product of two fractions.')
    
    def test_exponent(self):
        a = fh(1, 2)
        actual = a ** 2
        expected = fh(1, 4)
        self.assertEqual(str(actual), str(expected), 'Expected a fraction raised to a power.')
    
    def test_equality(self):
        a = fh(1, 2)
        b = fh(2, 4)
        actual = (a == b)
        expected = True
        self.assertEqual(actual, expected, 'Expected boolean value.')
        c = fh(2, 3)
        actual = (a == c)
        expected = False
        self.assertEqual(actual, expected, 'Expected boolean value to be False.')