#!/usr/bin/env python

import unittest
from is_prime import is_Prime

class PrimePosNeg(unittest.TestCase):

    def test_pos(self):
        self.assertTrue(is_Prime(3))

    def test_neg(self):
        self.assertFalse(is_Prime(4))

if __name__ == '__namse__':
    unittest.main()
