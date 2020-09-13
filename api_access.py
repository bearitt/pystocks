import yfinance as yf

def stock_lookup(symbol):
    #get Ticker object for stock symbol from user input
    stock = yf.Ticker(symbol)
    sInfo = stock.info
    #create dictionary with important info from Ticker
    important_info = {
            'Company':sInfo['shortName'],
            'Symbol':sInfo['symbol'],
            'Sector':sInfo['sector'],
            'Exchange':sInfo['exchange'],
            'Current Price':sInfo['regularMarketPrice'],
            'Dividend Yield':sInfo['dividendYield'],
            'Price to Earnings Ratio':sInfo['trailingPE'],
            'Market Cap':sInfo['marketCap'],
            'One year low/high':str(str(sInfo['fiftyTwoWeekLow']) + "/" + str(sInfo['fiftyTwoWeekHigh'])),
            'Summary':sInfo['longBusinessSummary'],
            'Website':sInfo['website']}
    #return dictionary with important stock ticker info
    return important_info

