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
        expected = 1
        self.assertEqual(str(actual.reduce()), str(expected), 'Expected reduced form of fraction.')
