import pandas as pd

#Filtering = Keeping the rows that match a condition

#df = pd.read_csv("example-data/mifania_employee_data.csv")
df = pd.read_json("example-data/mifania_student_data.json")

# old_employee = df[df["Age"] >= 40]
#retiring = df[df["Years_of_Experience"] >= 35]

good_students = df[(df["GPA"] >= 2) & (df["GPA"] < 3)] #Multiple condition i.e & | etc. (make sure to enclosed the with ())

print(good_students.to_string())