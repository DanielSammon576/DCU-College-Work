#!/usr/bin/env python

import unittest
from add_two_num import add

class TestAdd(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(add(1,1), 2, "Thsi is maybe a reason why the test is failing over and over again")

    def test_notequal(self):
        self.assertNotEqual(add(1,1), 3)

if __name__ == "__main__":
    unittest.main()


