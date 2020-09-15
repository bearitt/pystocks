import unittest
from packages.ui import *
import http

class TestApiAccess(unittest.TestCase):
    # only print_stock tested with unit test
    # to make sure function is passing arguments correctly and handling exceptions
    def test_types(self):
        # test to make sure exception raised with improper input
        # check for AttributeError since the yfinance Ticker class
        # performs .upper on argument passed
        self.assertRaises(AttributeError, print_stock, True)
        self.assertRaises(AttributeError, print_stock, 123)
        # index error should be thrown since an empty dictionary should be
        # returned from api with incorrect stock symbol
        self.assertRaises(ValueError, print_stock, 'not_a_stock_symbol')
        # invalid url since spaces used
        self.assertRaises(http.client.InvalidURL, print_stock, 'not a stock symbol')
