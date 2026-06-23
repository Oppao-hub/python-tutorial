# Python file detection

from genericpath import isdir
import os

current_dir = os.path.dirname(__file__)

file_path1 = f"{current_dir}/test"
file_path2 = "/Users/mifaniapaolo0012/Desktop/Mifania System/Documents/Asset.svg"
file_path3 = "/Users/mifaniapaolo0012/Desktop/Mifania System/Documents"

if os.path.exists(file_path1):
    print(f"The location '{file_path2}' exist")

    if os.path.isfile(file_path2):
        print("That is a file")
    elif os.path.isdir(file_path2):
        print("This is a directory")
else:
    print(f"The location '{file_path2}' doen't exist")