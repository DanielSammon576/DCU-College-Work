import unittest
from is_teenager import is_Teenager

a = [1.0, 20, 0, -1, " ", "", None, True]
b = [13, 14, 15, 16, 17, 18, 19]

class TeenagerTestClass(unittest.TestCase):

    def test_pos(self):
        self.assertTrue(is_Teenager(16))

    def test_neg(self):
        for i in a:
            self.assertFalse(is_Teenager(i))

if __name__ == '__main__':
    unittest.main()
