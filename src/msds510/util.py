# Mary Kay Kincaid
# 4/25/18
# Midterm Assignment

# imports

import csv
import operator as op


def convert_to_utf8(input, output):
    """Convert input of binary file to ouput file in UTF8."""
    f = open(input, encoding='iso-8859-1')
    data = f.read()

    with open(output, 'w', encoding='UTF-8') as f:
        f.write(data)


def write_csv(input, output):
    """Opens a UTF8 file and does several manipulations on values then
    outputs the header row and additional file rows to a new file."""
    current_year = 2018
    with open(input) as fin:
        dr = csv.DictReader(fin, delimiter=',')
        # dr = csv.DictReader(open(input))
        dr.fieldnames = [name.lower() for name in dr.fieldnames]
        dr.fieldnames = [name.strip('\n').strip('?') for name in dr.fieldnames]
        dr.fieldnames = [name.replace(' ', '_') for name in dr.fieldnames]
        dr.fieldnames = [name.replace('/', '_') for name in dr.fieldnames]
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
                dw.writerow(row)


def read_csv_dict(input):
    """Reads input file, converts to dict and sorts out data by number of appearances
    writes new list order to file."""
    list_of_dicts = []
    with open('../data/processed/avengers_processed.csv', 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            list_of_dicts.append(line)
            line['appearances'] = int(line['appearances'])

        list_of_dicts.sort(key=op.itemgetter('appearances'), reverse=True)

        with open('../data/processed/avengers_sorted.csv', 'w') as fou:
            dw = csv.DictWriter(fou, delimiter=',',
                                fieldnames=reader.fieldnames,
                                lineterminator='\n')
            headers = {}
            for n in dw.fieldnames:
                headers[n] = n
            dw.writerow(headers)
            for row in list_of_dicts:
                dw.writerow(row)


def create_report(input):
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
