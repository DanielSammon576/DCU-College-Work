#!/usr/bin/env python

import unittest
from add import add

class AddPosNegTestCase(unittest.TestCase):

    def test_pos(self):
        self.assertEqual(add(1,1), 2)

    def test_neg(self):
        self.assertNotEqual(add(1,1), 3)

if __name__ == '__main__':
    unittest.main()
