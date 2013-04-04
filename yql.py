import urllib
import urllib2

YQL_BASE = "http://query.yahooapis.com/v1/public/yql?"

class Query:
    output = "json"

    def build_url(self):
        raise "Abstract"

    def submit(self):
        url = self.build_url()
        response = urllib2.Request(url).read()
        return response


class SingleQuery(Query):
    stock = ""

    def __init__(self, stock):
        self.stock = stock

    def build_url(self):
        return YQL_BASE + urllib.urlencode([("stock", stock)])

class MultipleQuery(Query):
    stocks = []

    def __init__(self, stocks):
        self.stocks = stocks
