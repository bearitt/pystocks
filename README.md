# pystocks
Simple command line interface written in Python to access stock information on US exchanges. Created for COSC 499 assignment 1.

## Dependencies
* Python
* Yahoo finance API
    * pip install yfinance

## Usage guide
The program is run from the command line; compile and run pystocks.py.

##Modules
*api-access.py
    *Accesses Yahoo Finance API. Has a single function stock_lookup, which takes a stock symbol string argument and returns a dictionary containing basic information about the stock.
