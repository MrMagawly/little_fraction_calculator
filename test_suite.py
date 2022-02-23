#! usr/bin/python3

import unittest
import fractions_handler as fh

class TestFractionExpressions(unittest.TestCase):
    
    def test_addition(self):
        actual = fh.add(1, 2, 1, 3)
        expected = (5, 6)
        self.assertEqual(actual, expected, 'Expected sum of two fractions.')
        actual = fh.add(1, 2, 1, 2)
        expected = (2, 2)
        self.assertEqual(actual, expected, 'Expected sum of two fractions.')
        actual = fh.add(1, 3, 2, 2)
        expected = (8, 6)
        self.assertEqual(actual, expected, 'Expected sum of two fractions.')
