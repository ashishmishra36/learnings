import os
import csv
import requests
import re


def read_lines():
    # Open the file
    data = open('example.csv',encoding='utf-8')
    a = []
    # csv reader
    csv_data = csv.reader(data)

    # reformat it into a list of list
    csv_lines = list(csv_data)
    header = csv_lines[0]
    for x in csv_lines:
        if x[4] == 'Y':
            a = x
            break
    data.close()
    return dict(zip(header,a))

def write_lines():
    output = open('output_file.csv', mode='a+',newline='')
    csv_writer= csv.writer(output,delimiter=',')
    csv_writer.writerow([1,2,3,4,5])
    output.close()
###################################Excercise##############################################################
### Task One: Grab the Google Drive Link from .csv File
def find_diagonal():
    # when reading csv file use encoding
    file_to_read = open('find_the_link.csv', encoding='utf-8')
    csv_reader = csv.reader(file_to_read)
    drive_link = ''
    # it will return list of list
    data_as_list = list(csv_reader)
    # start from 0th get 0th, from 1st get 1st, from 2nd get 2nd ....
    i = 0
    for x in data_as_list:
        drive_link = drive_link+ x[i]
        i = i+1
    return drive_link

# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.
def download_file():
    l = find_diagonal()
    pattern = '=.+'
    id = re.findall(pattern,l)[0][1:]
    # what we are getting in l is just for viewing the URL but
    # Google uses "uc?export=download&id=" To download a file directly
    base= 'https://docs.google.com/uc?export=download&id=' + id
    response = requests.get(base, stream=True)
    # read the file in binary mode - use "wb"
    file_data = open('udemy.pdf', mode='wb')
    for x in response.iter_content(32768):
        if x:
            file_data.write(x)
    file_data.close()

download_file()

def find_phone_numer():
    my_file = open('udemy.pdf', 'rb')
    f= my_file.readlines()
    print(f)
    data_list = list(f)
    pattern = r'^\d{3}-\d{3}-\d{4}'
    for x in f:
        p = re.findall(pattern,x)
    print(p)


def file_data():
    base_dir = os.path.abspath(__file__)
    f = os.path.dirname(__file__)
    print(base_dir)
    test = os.path.join(f,'gfg/modules.txt')
    my_file = open(test)
    content = my_file.read()
    print(content)


file_data()