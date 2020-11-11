#!/usr/bin/env python

import unittest
from is_prime import is_Prime

class PrimesTestCase(unittest.TestCase):

    def test_is_five_prime(self):
        self.assertTrue(is_Prime(5))

if __name__=='__main__':
    unittest.main()
