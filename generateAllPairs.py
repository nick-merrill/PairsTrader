#!/usr/bin/python

import sys
import subprocess
import csv
from pairGenerator import *
from progress import *

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

progress = Progress(len(combos))

i = 0
errors = 0
for row in combos:
    stock1 = row[0]
    stock2 = row[1]

    try:
        merge_adjusted_prices(stock1, stock2, "data", "pairs")
    except:
        errors += 1

    i += 1
    progress.update(i)
