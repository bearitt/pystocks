import unittest
from api_access import *
import http

class TestApiAccess(unittest.TestCase):
    def test_access(self):
        #test to make sure api is properly accessed
        self.assertEqual(stock_lookup('INTC')['Symbol'],'INTC')
    def test_types(self):
        #test to make sure exception raised with improper input
        #check for AttributeError since the yfinance Ticker class
        #performs .upper on argument passed
        self.assertRaises(AttributeError, stock_lookup, True)
        self.assertRaises(AttributeError, stock_lookup, 123)
        #index error should be thrown since an empty dictionary should be
        #returned from api with incorrect stock symbol
        self.assertRaises(ValueError, stock_lookup, 'not_a_stock_symbol')
        #invalid url since spaces used
        self.assertRaises(http.client.InvalidURL, stock_lookup, 'not a stock symbol')
