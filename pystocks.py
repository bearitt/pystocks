from api_access import *

print("Welcome to Pystocks!")
intel = 'INTC'
stock_info = stock_lookup(intel)
for key in stock_info:
    print(str(key) + ": " + str(stock_info[key]))
