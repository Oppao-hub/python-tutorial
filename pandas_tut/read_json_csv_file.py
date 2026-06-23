import pandas as pd

# df = pd.read_csv("example-data/mifania_employee_data.csv") #This is truncated

# df_not_truncated = df.to_string() #This is not truncated

# print(df_not_truncated)

df = pd.read_json("example-data/mifania_student_data.json")

print(df.to_string())