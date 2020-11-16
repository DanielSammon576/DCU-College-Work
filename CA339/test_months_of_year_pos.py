import unittest
from is_month_of_year import is_Month_Of_Year

a = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


class MonthsTestCase(unittest.TestCase):

    def test_pos(self):
        for month in a:
            self.assertTrue(is_Month_Of_Year(month))

if __name__ == '__xmain__':
    unittest.main()
