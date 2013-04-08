import urllib
import urllib2

YQL_BASE = "http://query.yahooapis.com/v1/public/yql?"
QUOTES_DB = "yahoo.finance.quotes"

class Query:
    output = "json"

    def yql_format(self):
        raise "Abstract"

    def submit(self):
        yql_query = self.yql_format()
        print yql_query
        url = YQL_BASE + urllib.urlencode([("q", yql_query)])
        print url
        response = urllib2.urlopen(url).read()
        return response

class Date:
    year = 0
    month = 0
    day = 0
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def yql_format(self):
        # TODO: this has improper formatting (four digit year, etc.)
        # use python date class
        return str(self.year) + '-' + str(self.month) + '-' + str(self.day)

class Lookup(Query):
    stocks = []

    start_date = None
    end_date = None

    def __init__(self, stocks):
        self.stocks = stocks

    def yql_format(self):
        stocks = []
        for stock in self.stocks:
            stocks.append('"' + stock + '"')
        yql_query = "select * from " + QUOTES_DB + " where symbol in (" \
                     + (",".join(stocks)) + ")"
        if start_date:
            yql_query += ' and startDate = "' + self.start_date.yql_format() + '"'
        if end_date:
            yql_query += ' and startDate = "' + self.end_date.yql_format() + '"'
        return yql_query
