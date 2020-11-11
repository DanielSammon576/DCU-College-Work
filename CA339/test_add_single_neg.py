#!/usr/bin/env python

import unittest
from add import add

class AddPosNegTestCase(unittest.TestCase):

    def test_is_1_plus_1_not_2(self):
        self.assertNotEqual(add(1,1), 3)

if __name__ == '__main__':
    unittest.main()
