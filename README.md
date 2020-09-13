# pystocks
Simple command line interface written in Python to access stock information on US exchanges. Created for COSC 499 assignment 1.

## Dependencies
* Python
* Yahoo finance API
    * ```
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
* output.py
    * Outputs the result of a stock lookup to a file. Contains five methods:
        1. date_format: returns a string version of the current date and time.
        2. check_for_dir: checks for the existence of a subdirectory of the parent directory called 'reports' and creates the directory if it does not exist.
        3. output_txt: outputs a .txt file containing the stock information.
        4. output_json: outputs a .json file containing the stock information.
        5. output_csv: outputs a .csv file containing the stock information.
