#!/usr/bin/python

import sys
from os import path
import urllib
import csv

base_url = "http://ichart.finance.yahoo.com/table.csv?s="
def make_url(ticker_symbol):
    return base_url + ticker_symbol

output_path = "."
def make_filename(ticker_symbol, directory="data"):
    return path.join(output_path, directory, ticker_symbol+".csv")

def pull_data(ticker_symbol, directory="data"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()

def csv_to_array(csv_file):
    rows = []
    reader = csv.reader(csv_file)
    for row in reader:
        rows.append(row)
    return rows

def is_match(o1, o2, match_col):
    return o1[match_col] == o2[match_col]

# Line up the columns side by side in the new CSV, being sure to
# match the "match condition" for each entry, e.g. "Date".
def merge_csv(name1, name2, mergable_col, match_col, \
              from_directory, to_directory, out_name):
    f1_name = path.join(from_directory, name1)
    f2_name = path.join(from_directory, name2)
    with open(f1_name+".csv", 'rb') as f1, open(f2_name+".csv", 'rb') as f2:
        a1 = csv_to_array(f1)
        a2 = csv_to_array(f2)

        old_header_row = a1.pop(0)
        a2.pop(0) # remove header row for other data sheet
        match_name = old_header_row[match_col]
        mergable_name = old_header_row[mergable_col]

        merged = []
        merged.append([match_name, "%s %s" % (name1, mergable_name), \
                   "%s %s" % (name2, mergable_name)])

        for row1 in a1:
            for row2 in a2:
                if is_match(row1, row2, match_col):
                    merged.append([row1[match_col], row1[mergable_col],
                                  row2[mergable_col]])
        f1.close()
        f2.close()

    out_file = path.join(to_directory, out_name+".csv")
    with open(out_file, "wb") as out:
        writer = csv.writer(out)
        writer.writerows(merged)
        out.close()


def merge_adjusted_prices(stock1, stock2, from_directory, to_directory):
    out_name = "%s-%s" % (stock1, stock2)

    # 6 is the adjusted close, and 0 is the date
    merge_csv(stock1, stock2, 6, 0, from_directory, to_directory, out_name)



#-----------------------------------------------------------------------------


stocks = []
i = 1
try:
    while (1):
        symbol = sys.argv[i]
        symbol = symbol.upper()
        print "Loaded %s" % symbol
        stocks.append(symbol)
        i += 1
except IndexError:
    if i == 1:
        print "You must pass at least one stock symbol."
        sys.exit()

pull_data(stocks[0])
pull_data(stocks[1])

merge_adjusted_prices(stocks[0], stocks[1], "data", "pairs")







