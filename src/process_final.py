# Mary Kay Kincaid
# 5/26/2018
# Week 11 - Final Project

import os
import sys
import operator
from src.msds510.utils.conversion import *


# main function
def main():
    """Main function to read in Avengers file and output modified data file."""
    convert_file_to_utf8('../data/raw/avengers.csv', '../data/processed/avengers_temp.csv')
    read_class_file('../data/processed/avengers_temp.csv', '../data/processed/avengers_processed.csv')
    query_yes_no('Run Markdown Report for Top 10 Avengers?')


if __name__ == "__main__":
    main()
