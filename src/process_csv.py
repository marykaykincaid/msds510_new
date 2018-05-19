# Mary Kay Kincaid
# 4/25/18
# Midterm Assignment

# imports


# functions used in this .py file
from msds510.util import convert_to_utf8
from msds510.util import write_csv


# main function
def main():
    """Main funciton to read in Avengers file and output modified data file."""
    convert_to_utf8('../data/raw/avengers.csv',
                    '../data/processed/avengers_temp.csv')
    write_csv('../data/processed/avengers_temp.csv',
              '../data/processed/avengers_processed.csv')


if __name__ == "__main__":
    main()
