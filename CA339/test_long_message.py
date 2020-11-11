#!/usr/bin/env python

import unittest
from add import add

class TestAddL(unittest.TestCase):

    def test_pos(self):
        self.assertEqual(add(1,2), 3, "There is a problem with the test, result does not match expected result")

if __name__ == '__main__':
    unittest.main()
