import pandas as pd

# SELECTION BY COLUMN/S
# df = pd.read_csv("example-data/mifania_employee_data.csv")

# Single column
# print(df["Employee_ID"].to_string())
# print(df["Age"].to_string())
# print(df["Gender"].to_string())

# Multiple column
# print(df[["Employee_ID", "Age", "Gender"]].to_string())


# SELECTION BY ROW/S

df = pd.read_csv("example-data/mifania_employee_data.csv", index_col="Employee_ID") #Set the column

#print(df.loc["EMP-2013"]) #All the column of the specific employee
#print(df.loc["EMP-2013", ["Age", "Gender"]]) #Specific column of the specific employee
#print(df.loc["EMP-2013":"EMP-2026", ["Age", "Gender"]]) #Range of rows
#print(df.iloc[0]) #Access by integer location
#print(df.iloc[0:11])  #Access by integer location with range
#print(df.iloc[0:11:2])  #Access by integer location with range and with steps
#print(df.iloc[0:11, 5])  #Access by integer location with range and specific columns
print(df.iloc[0:11, 0:5])  #Access by integer location with range and range of columns