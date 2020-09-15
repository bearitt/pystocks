from packages.api_access import *
from packages.output import *
import http

def welcome():
    print('Welcome to Pystocks!\n-----------------------------')
    input_message = 'Please input a stock symbol to see more information on the stock (note that only US market symbols are supported), or type in \'exit\' to exit the program :\n' 
    # obtain user input
    # loop until user inputs 'exit'
    symbol = ''
    while symbol.lower()!='exit':
        symbol = input(input_message)
        # check for 'exit' signal to skip api access
        if symbol.lower() == 'exit':
            continue
        print_stock(symbol)
    goodbye()

def print_stock(symbol):
        # try block for IndexError: catches exceptions thrown when
        # stock symbol lookup fails
        try:
            stock_info = stock_lookup(symbol)
            for key in stock_info:
                print(str(key) + ": " + str(stock_info[key]))
            file_prompt(stock_info)
        except IndexError:
            print('Sorry, we couldn\'t find a company matching that symbol')
        except http.client.InvalidURL:
            print('Sorry, we couldn\'t find a company matching that symbol')
        print('-----------------------------')

def file_prompt(stock_info):
    user_choice = -1
    none_flag = txt_flag = json_flag = csv_flag = False
    while not none_flag and not txt_flag and not json_flag and not csv_flag:
        print('''Would you like to output the results to a file?
    (Note that multiple file types can be output simultaneously, e.g. 13 will output a .txt file and a .csv file)
    0. No thank you
    1. .txt file
    2. .json file
    3. .csv file''')
    # boolean flag used to display correct error message with invalid user input
        is_string = False
    # try block catches ValueError: catches exceptions thrown when
    # user inputs a non-integer value
        user_choice = input('Your choice: ')
        try:
            int_user_choice = int(user_choice)
        # flags determine type of output desired, allows for multiple reports
        # to be generated
            none_flag = user_choice.find('0') != -1
            txt_flag = user_choice.find('1') != -1
            json_flag = user_choice.find('2') != -1
            csv_flag = user_choice.find('3') != -1
        except ValueError:
            print('That\'s not a number, try again!')
            is_string = True
        int_user_choice = None
        if none_flag:
            continue
        else:
            if txt_flag:
                output_txt(stock_info)
                print('Text file generated in reports directory')
            if json_flag:
                output_json(stock_info)
                print('JSON file generated in reports directory')
            if csv_flag:
                output_csv(stock_info) 
                print('CSV file generated in reports directory')
            elif not is_string:
                print('Invalid choice, try a number in the specified range!')

def goodbye():
    print('Thank you for using Pystocks!')
