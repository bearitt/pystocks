from api_access import *
from output import *

def user_search():
    symbol = input('Please input a stock symbol to see more information on the stock (note that only US market symbols are supported), or type in \'exit\' to exit the program :\n').upper()
    while symbol.lower()!='exit':
        try:
            stock_info = stock_lookup(symbol)
            for key in stock_info:
                print(str(key) + ": " + str(stock_info[key]))
            try:
                user_choice = -1
                while user_choice < 0 or user_choice > 3:
                    print('''Would you like to output the results to a file?
    0. No thank you
    1. .txt file
    2. .json file
    3. .csv file''')
                    user_choice = int(input('Your choice: '))
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
                    else:
                        print('Invalid choice, try again!')
            except ValueError:
                print('Invalid choice, try again!')
        except IndexError:
            print('Sorry, we couldn\'t find a company matching that symbol')
        print('-----------------------------')
        symbol = input('Please input a stock symbol to see more information on the stock (note that only US market symbols are supported), or type in \'exit\' to exit the program :\n').upper()

