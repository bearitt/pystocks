import yfinance as yf

def stock_lookup(symbol):
    #get Ticker object for stock symbol from user input
    stock = yf.Ticker(symbol)
    sInfo = stock.info
    #create dictionary with important info from Ticker
    important_info = {'Company':sInfo['shortName'],'Sector':sInfo['sector'],'Summary':sInfo['longBusinessSummary']}
    return important_info

