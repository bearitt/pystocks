from api_access import *
from output import *

def user_search():
    input_message = 'Please input a stock symbol to see more information on the stock (note that only US market symbols are supported), or type in \'exit\' to exit the program :\n' 
    #obtain user input
    #loop until user inputs 'exit'
    symbol = ''
    while symbol.lower()!='exit':
        symbol = input(input_message).upper()
        #check for 'exit' signal to skip api access
        if symbol.lower() == 'exit':
            continue
        #first try block for IndexError: catches exceptions thrown when
        #stock symbol lookup fails
        try:
            stock_info = stock_lookup(symbol)
            for key in stock_info:
                print(str(key) + ": " + str(stock_info[key]))
            user_choice = -1
            while user_choice < 0 or user_choice > 3:
                print('''Would you like to output the results to a file?
    0. No thank you
    1. .txt file
    2. .json file
    3. .csv file''')
        #boolean flag used to display correct error message with invalid user input
                is_string = False
        #nested try block catches ValueError: catches exceptions thrown when
        #user inputs a non-integer value
                try:
                    user_choice = int(input('Your choice: '))
                except ValueError:
                    print('That\'s not a number, try again!')
                    is_string = True
                if user_choice==0:
                    continue
                elif user_choice==1:
                    output_txt(stock_info)
                    print('Text file generated in reports directory')
                elif user_choice==2:
                    output_json(stock_info)
                    print('JSON file generated in reports directory')
                elif user_choice==3:
                    output_csv(stock_info) 
                    print('CSV file generated in reports directory')
                elif (user_choice<0 or user_choice>3) and not is_string:
                    print('Invalid choice, try a number in the specified range!')
        except IndexError:
            print('Sorry, we couldn\'t find a company matching that symbol')
        print('-----------------------------')
