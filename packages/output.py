from packages.api_access import *
from datetime import *
import os

def output_txt(dictionary):
    check_for_dir()
    txt_file = open('./reports/' + str(dictionary['Symbol'])+date_format() + '.txt','w')
    for key in dictionary:
    #no special formatting for txt files
        txt_file.writelines(key + ": " + str(dictionary[key]) + '\n')
    txt_file.close()
    return

def output_json(dictionary):
    check_for_dir()
    json_file = open('./reports/' + str(dictionary['Symbol'])+date_format() + '.json','w')
    json_file.writelines('{')
    counter = 0
    for key in dictionary:
    #enclose each key and value with double quotes with a colon separating key:value
        json_file.writelines('"' + key + '":"' + str(dictionary[key]) + '"')
        if counter != len(dictionary) - 1:
            json_file.write(',')
            counter += 1
    json_file.write('}')
    json_file.close()
    return
#note: json output validated on jsonlint.com for correctness

def output_csv(dictionary):
    check_for_dir()
    csv_file = open('./reports/' + str(dictionary['Symbol']) + date_format() + '.csv','w')
    for key in dictionary:
    #if a field contains a comma, enclose in double quotes as per csv standards
        if str(dictionary[key]).find(',') != -1:
            csv_file.writelines(key + ',' + '"' + str(dictionary[key] + '"' + '\n'))
        else:
            csv_file.writelines(key + ',' + str(dictionary[key]) + '\n')
    csv_file.close()
    return

def date_format():
    return str(datetime.now()).replace(' ','--')

#check for 'reports' directory, create if does not exist
def check_for_dir():
    report = './reports'
    if not os.path.exists(report):
        os.makedirs(report)
