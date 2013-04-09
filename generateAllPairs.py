#!/usr/bin/python

import sys
import subprocess
import csv
from pairGenerator import *

def csv_to_array(csv_file):
    rows = []
    reader = csv.reader(csv_file)
    for row in reader:
        rows.append(row)
    return rows

try:
    symbols_file_name = sys.argv[1]
except IndexError:
    if len(sys.argv) < 2:
        print "You must pass the combinations file name."
        sys.exit()

with open(symbols_file_name, "rU") as f:
    combos = csv_to_array(f)
    combos.pop(0)
    f.close()

for row in combos:
    stock1 = row[0]
    stock2 = row[1]
    print stock1
    print stock2

    pull_and_merge(stock1, stock2)

    print ""
