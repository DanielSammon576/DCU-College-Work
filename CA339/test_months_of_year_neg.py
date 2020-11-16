import unittest
from is_month_of_year import is_Month_Of_Year

a = [0.0, 0, "jan", None, ""]

class MonthsTestCase(unittest.TestCase):

    def test_neg_November(self):
        for i in a:
            self.assertFalse(is_Month_Of_Year(i))

if __name__ == '__main__':
    unittest.main()

