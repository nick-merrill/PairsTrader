#!/usr/bin/python

from StockScraper import stockretriever
stocks = stockretriever.StockRetriever()

info = stocks.get_current_info(["AAPL","GOOG"])

print info["LastTradeWithTime"]
