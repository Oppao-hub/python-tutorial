import pandas as pd

#aggregate function = Reduces a set of values into a single summary value
#                     Used to summarize and analyze data
#                     Often used with the groupby() function

df = pd.read_json("example-data/mifania_student_data.json")

#-------------------WHOLE DATAFRAME-------------------

# print("MEAN")
# print(df.mean(numeric_only=True)) #Show the mean of all numeric values
# print()

# print("SUM")
# print(df.sum(numeric_only=True)) #Show all the sum of all numeric values
# print()

# print("MINIMUM")
# print(df.min(numeric_only=True)) #Show all the minimum of all numeric values
# print()

# print("MAXIMUM")
# print(df.max(numeric_only=True)) #Show all the maximum of all numeric values
# print()

# print("COUNT")
# print(df.count()) #Count all the values in the column
# print()

#-------------------SINGLE COLUMN-------------------
# print(f"MEAN: {df["GPA"].mean()}")
# print(f"SUM: {df["GPA"].sum()}")
# print(f"MINIMUM: {df["GPA"].min()}")
# print(f"MAXIMUM: {df["GPA"].max()}")
# print(f"NUMBER OF ROWS: {df["GPA"].count()}")

#-------------------GROUP BY-------------------
gender_group = df.groupby("Gender")

print(gender_group["Age"].mean())
print(gender_group["Age"].sum())
print(gender_group["Age"].min())
print(gender_group["Age"].max())
print(course_group["Age"].count())
