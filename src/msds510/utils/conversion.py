# Mary Kay Kincaid
# 5/26/2018
# Week 11 - Final Project

import os
import sys
import operator
import csv
from src.msds510.avenger_final import *


def convert_file_to_utf8(input, output):
    """Convert input of binary file to output file in UTF8."""
    f = open(input, encoding='iso-8859-1')
    data = f.read()

    with open(output, 'w', encoding='UTF-8') as f:
        f.write(data)


def convert_to_python_friendly(original_name):
    """Convert the dictinoary headers to code friendly names"""
    original_name = original_name.lower()
    original_name = original_name.strip('\n').strip('?')
    original_name = original_name.replace(' ', '_')
    original_name = original_name.replace('/', '_')
    return original_name


def read_class_file(input, output):
    """Opens a UTF8 file and does several manipulations on values then
    outputs the header row and additional file rows to a new file."""
    current_year = 2018
    with open(input) as fin:
        dr = csv.DictReader(fin, delimiter=',')

        dr.fieldnames = [convert_to_python_friendly(name) for name in dr.fieldnames]
        dr.fieldnames.append('month_joined')

        # dr.fieldnames contains values from first row of `f`.
        # for row in dr:
        # print(row)

        with open(output, 'w') as fou:
            dw = csv.DictWriter(fou, delimiter=',',
                                fieldnames=dr.fieldnames, lineterminator='\n')
            headers = {}
            for n in dw.fieldnames:
                headers[n] = n
            dw.writerow(headers)
            for row in dr:
                row['appearances'] = int(row['appearances'])
                row['years_since_joining'] = int(row['years_since_joining'])
                row['years_since_joining'] = current_year - int(row['year'])
                row['notes'] = row['notes'].strip('\n').rstrip()

                words = {'death1', 'return1', 'current', 'death2',
                         'return2', 'death3', 'return3', 'death4',
                         'return4', 'death5', 'return5'}
                for i in row:
                    if i in words:
                        row[i] = bool(row[i])
                class_data = Avenger(row)
                dw.writerow(row)


def to_markdown(input):
        """Outputs a report based on the sorted file data."""
        with open('../data/processed/avengers_sorted.csv', 'r') as f:
            reader = csv.DictReader(f)
            print("Avengers Markdown Report")
            for i, row in enumerate(reader):
                print('#', i+1, '.', row['name_alias'], '\n')
                print('* Number of Appearances:', row['appearances'])
                print('* Year Joined:', row['year'])
                print('* Years Since Joining:', row['years_since_joining'])
                print('* URL:', row['url'], '\n')
                print('## Notes\n')
                print(row['notes'], '\n\n')
                if i >= 9:
                    break


def query_yes_no(question, default='yes'):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    valid_yes = {"yes": True, "y": True, "ye": True}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid_yes:
            to_markdown('../data/processed/avengers_sorted.csv')
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

# Change input to int
def to_int(field_to_int):
    """Convert argument to integer."""
    return int(field_to_int)


# Change input to boolean
def to_bool(field_to_bool):
    """Convert argument to boolean."""
    if field_to_bool == 'YES':
        return bool(field_to_bool)
    if field_to_bool == 'NO':
        return bool(field_to_bool)
    if field_to_bool == '':
        return bool(field_to_bool)
