#!/usr/bin/python

from yql import *

q = Lookup(["AAPL"])

q.submit()
