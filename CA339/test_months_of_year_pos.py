import unittest
from is_month_of_year import is_Month_Of_Year

class MonthsTestCase(unittest.TestCase):

    def test_November(self):
        self.assertTrue(is_Month_Of_Year("November"))

if __name__ == '__main__':
    unittest.main()
