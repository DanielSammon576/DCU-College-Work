import unittest
from is_month_of_year import is_Month_Of_Year

class MonthsTestCase(unittest.TestCase):

    def test_neg_November(self):
        self.assertFalse(is_Month_Of_Year("Novembar"))

if __name__ == '__main__':
    unittest.main()

