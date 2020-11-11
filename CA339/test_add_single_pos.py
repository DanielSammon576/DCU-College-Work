#!/usr/bin/env python

import unittest
from add import add

class AddTestCase(unittest.TestCase):

    def test_is_1_plus_1_2(self):
        self.assertEqual(add(1,1), 2)

if __name__ == '__main__':
    unittest.main()
