#!/usr/bin/env python

import unittest
from test_prime_number_pos_neg import TestIsPrimeNumber
from test_add_single_pos_neg import TestAddition

def my_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIsPrimeNumber))
    suite.addTest(unittest.makeSuite(TestAddition))
    run = unittest.TextTestRunner()
    print(run.run(suite))

my_suite()
