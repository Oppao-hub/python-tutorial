# Python writing files (.txt, .json, .csv)

import json
import csv

text_data = "I like pizza!"

file_path1 = "/Users/mifaniapaolo0012/Desktop/Python/oop/files/output.txt"

# 'w' = to write 
# 'x' = to write if it doesn't exist
# 'r' = to read
# 'a' = to append

# try:
#     with open(file=file_path1, mode="x") as file:
#         file.write(text_data + "\n")
#         print(f"Text file '{file_path1}' was created")
# except FileExistsError:
#     print(f"The file '{file_path1}' already exist!")


#JSON
# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "Cook",
# }

# file_path2 = "/Users/mifaniapaolo0012/Desktop/Python/oop/files/output.json" #create the file in the desktop
# try:
#     with open(file=file_path2, mode="w") as file:
#         json.dump(employee, file, indent=4) #convert dictionary to json string
#         print(f"Text file '{file_path2}' was created")
# except FileExistsError:
#     print(f"The file '{file_path2}' already exist!")

#CSV
employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"],
]

file_path = "/Users/mifaniapaolo0012/Desktop/Python/oop/files/output.csv"

try:
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print(f"The file '{file_path}' already exist!")