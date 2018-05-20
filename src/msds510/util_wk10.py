# Mary Kay Kincaid
# 5/19/2018
# Assignment 10.1 - Week 10 - Exception Handling

"""
Functions for converting to integer, checking if dictionary
or list value and getting dates
"""

from datetime import datetime


# Change input to int
def to_int(field_to_int):
    """Convert argument to integer."""
    try:
        i = int(field_to_int)
        # print(i)
        return i
    except:
        # print('Not an integer')
        return None


def get_value(item, position):
    """Returns integer index if input is sequence, Returns index key value if input is dictionary"""
    try:
        return item.index(position)
    except:
        try:
            return item[position]
        except:
            return None

# if dict, get key[value], or list get index of where item is


def get_date(d):
        """
        Returns:
            datetime.date: The date the character joined the Avengers
        """
        try:
            new_d = datetime.strptime(d, '%b-%y')
            day = str(new_d.day)
            month = str(new_d.month)
            year = str(new_d.year)
            new_date_string = month + '-' + day + '-' + year
            date_joined = datetime.strptime(new_date_string, '%m-%d-%Y')
            date_joined = datetime.date(date_joined)
            new_year = date_joined.year
            new_month = date_joined.month
            new_day = date_joined.day
            return date_joined
        except:
            return None
