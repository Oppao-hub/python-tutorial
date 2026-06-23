# Python reading files (.txt, .json, .csv)

import json
import csv

txt_file_path = "/Users/mifaniapaolo0012/Desktop/Python/oop/files/input.txt"
json_file_path = "/Users/mifaniapaolo0012/Desktop/Python/oop/files/input.json"
csv_file_path = "/Users/mifaniapaolo0012/Desktop/Python/oop/files/input.csv"

#READ TXT
# try:
#     with open(txt_file_path, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")


#READ JSON
# try:
#     with open(json_file_path, 'r') as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")

#READ CSV
try:
    with open(csv_file_path, 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line) #you can print the index 0 1 2 etc.
except FileNotFoundError:
    print("That file was not found")