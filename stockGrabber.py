import urllib2
urlopen = urllib2.request.urlopen
urlEncode = urllib2.urlencode

# From example at http://developer.yahoo.com/yql/guide/yql-code-examples.html#sdk_yql

BASE_URL = "http://query.yahooapis.com/v1/yql"

results = ""

# query to get airport data for SFO airport
query = "SELECT * from geo.places WHERE text='SFO'"

# callback function for handling response data
def handler(rsp):
    if rsp.data:
        results = rsp.data

def toQueryString(obj):
    parts = []
    for each in obj:
        if obj.hasOwnProperty(each):
            parts.push(urlEncode(each) + '=' + urlEncode(obj[each]))
    return parts.join('&')

urlopen(BASE_URL)
