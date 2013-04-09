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
    stocks = csv_to_array(f)
    stocks.pop(0)
    f.close()

progress = Progress(len(stocks))

i = 0
errors = 0
for row in stocks:
    try:
        stock = row[0]
    except:
        errors += 1
    pull_data(stock)
    i += 1
    progress.update(i)

print "Errors: %d" % errors
