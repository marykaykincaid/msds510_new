# Mary Kay Kincaid
# 5/26/2018
# Week 11 - Final Project

"""
Unit Testing functions
"""

from msds510.util_wk10 import*
import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        self.name_alias = 'Henry Jonathan "Hank" Pym'
        self.url = 'http://marvel.wikia.com/Henry_Pym_(Earth-616)'
        self.appearances = '1269'
        self.current = 'YES'
        self.death1 = 'YES'
        self.death2 = ''
        self.death3 = ''
        self.death4 = ''
        self.death5 = ''
        self.full_reserve_avengers_intro = 'Sep-63'
        self.gender = 'MALE'
        self.honorary = 'Full'
        self.notes = 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n'
        self.probationary_introl = ''
        self.return1 = 'NO'
        self.return2 = ''
        self.return3 = ''
        self.return4 = ''
        self.return5 = ''
        self.year = '1963'
        self.years_since_joining = '52'

    def test_int_input(self):
        check_int = to_int(self.appearances)
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
