import unittest
from is_teenager import is_Teenager

a = [13,14,15,16,17,18,19]
b = ["abc", "", 12, 20, 16.2, -3, None, 0]


class TeenTestCase(unittest.TestCase):

    def test_pos(self):
        for num in a:
            self.assertTrue(is_Teenager(num))

    def test_neg(self):
        for num in b:
            self.assertFalse(is_Teenager(num))

if __name__ == '__main__':
    unittest.main()
