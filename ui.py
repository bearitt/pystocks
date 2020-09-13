from api_access import *
def user_search():
    symbol = input('Please input a stock symbol to see more information on the stock (note that only US market symbols are supported), or type in \'exit\' to exit the program :\n').upper()
    while symbol.lower()!='exit':
        try:
            stock_info = stock_lookup(symbol)
            for key in stock_info:
                print(str(key) + ": " + str(stock_info[key]))
        except IndexError:
            print('Sorry, we couldn\'t find a company matching that symbol')
        print('-----------------------------')
        symbol = input('Please input a stock symbol to see more information on the stock (note that only US market symbols are supported), or type in \'exit\' to exit the program :\n').upper()
