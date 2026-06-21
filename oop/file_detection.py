# Python file detection

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist")
else:
    print(f"The location '{file_path}' doen't exist")