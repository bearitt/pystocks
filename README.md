# pystocks
Simple command line interface written in Python to access stock information on US exchanges. Created for COSC 499 assignment 1.

## Dependencies
* Python
* Yahoo finance API
```
    pip install yfinance
```

## Usage guide
The program is run from the command line; open a terminal in the parent directory and type
```
python pystocks.py
```

## Modules
* pystocks.py
    * Main method, calls ui.py to start the user interface.
* api-access.py
    * Accesses Yahoo Finance API. Has a single function stock_lookup, which takes a stock symbol string argument and returns a dictionary containing basic information about the stock.
* ui.py
    * Creates a simple UI for the user to input stock symbols to lookup. Has a single function, user_search, which prompts the user for a stock symbol, then call stock_lookup and returns the information for the selected company. The method loops until the user types 'exit'.
