#!/usr/bin/python

import sys
import subprocess
import csv
from pairGenerator import *
from progress import *

import numpy
import stattools

i = 0
errors = 0

try:
    stock1 = sys.argv[1].upper()
    stock2 = sys.argv[2].upper()
except IndexError:
    print "Pass two stocks please!"
    sys.exit()

print stock1
print stock2

pull_data(stock1)
pull_data(stock2)

merge_adjusted_prices(stock1, stock2, "data", "pairs")



i += 1
