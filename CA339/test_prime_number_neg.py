#!/usr/bin/env python

import unittest
from is_prime import is_Prime

class TestPrimeNeg(unittest.TestCase):

    def test_neg(self):
        self.assertFalse(is_Prime(4))

if __name__ == '__main__':
    unittest.main()
