from api_access import *
from datetime import *
import os

def output_txt(dictionary):
    check_for_dir()
    txt_file = open('./reports/' + str(dictionary['Symbol'])+date_format() + '.txt','w')
    for key in dictionary:
        txt_file.writelines(key + ": " + str(dictionary[key]) + '\n')
    txt_file.close()
    return

def output_json(dictionary):
    check_for_dir()
    json_file = open('./reports/' + str(dictionary['Symbol'])+date_format() + '.json','w')
    json_file.writelines('{')
    for key in dictionary:
        json_file.writelines(key + ':' + str(dictionary[key]))
    json_file.write('}')
    json_file.close()
    return

def output_csv(dictionary):
    check_for_dir()
    csv_file = open('./reports/' + str(dictionary['Symbol']) + date_format() + '.csv','w')
    for key in dictionary:
        if str(dictionary[key]).find(',') != -1:
            csv_file.writelines(key + ',' + '"' + str(dictionary[key] + '"' + '\n'))
        else:
            csv_file.writelines(key + ',' + str(dictionary[key]) + '\n')
    csv_file.close()
    return

def date_format():
    return str(datetime.now()).replace(' ','--')

def check_for_dir():
    report = './reports'
    if not os.path.exists(report):
        os.makedirs(report)
