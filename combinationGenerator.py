#!/usr/bin/python

import sys
from os import path
import csv
import itertools

def csv_to_single_array(csv_file, col_num):
    rows = []
    reader = csv.reader(csv_file)
    for row in reader:
        try:
            rows.append(row[col_num])
        except IndexError:
            pass
    return rows

try:
    symbols_file_name = sys.argv[1]
    out_name = sys.argv[2]
except IndexError:
    if len(sys.argv) < 3:
        print "You must pass the symbols' file name AND an outfile name."
        sys.exit()

with open(symbols_file_name, "rU") as f:
    symbols = csv_to_single_array(f, 0)
    symbols.pop(0)
    f.close()

combos_iterable = itertools.combinations(symbols, 2)

combos = []
for c in combos_iterable:
    combos.append(c)

with open(out_name, "wb") as out:
    writer = csv.writer(out)
    writer.writerows(combos)
    out.close()




