import unittest
from is_teenager import is_Teenager

class TeenagerTestClass(unittest.TestCase):

    def test_pos(self):
        a = [13,14,15,16,17,18,19]
        for i in a:
            if i in a:
                self.assertTrue(is_Teenager(i))

    def test_neg(self):
        a = [13,14,15,16,17,18,19]
        for i in a:
            if i not in a:
                self.assertFalse(is_Teenager(i))

if __name__ == '__main__':
    unittest.main()
