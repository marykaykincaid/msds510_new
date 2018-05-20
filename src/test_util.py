# Mary Kay Kincaid
# 5/19/2018
# Assignment 10.1 - Week 10 - Exception Handling

"""
Unit Testing for get_value, to_int and get_date functions
"""

from msds510.util_wk10 import*
import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        self.x = {'a': 1, 'b': 52, 'd': 6}
        self.y = ['a', 'c', 'd']

    def test_int_input(self):
        check_int = to_int(3)
        self.assertTrue(type(check_int) == int)

    def test_float_str(self):
        check_int = to_int(3.0)
        self.assertTrue(type(check_int) == int)

    def test_invalid_str(self):
        check_int = to_int('Bob')
        self.assertTrue(type(check_int) != int)

    def test_valid_dict_input(self):
        self.assertTrue(get_value(self.x, 'a') == 1)

    def test_dict_missing_key(self):
        self.assertIsNone(get_value(self.x, 'g'))

    def test_valid_list_input(self):
        self.assertTrue(get_value(self.y, 'd') == 2)

    def test_invalid_list_input(self):
        self.assertIsNone(get_value(self.y, 'b'))

    def test_get_date(self):
        self.assertTrue(str(get_date('Jan-72')) == '1972-01-01')

if __name__ == '__main__':

    unittest.main()
