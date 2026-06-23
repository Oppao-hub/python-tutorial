import pandas as pd

#Data cleaning = the process of fixing/removing:
#                incomplete, incorrect, or irrelevant data.
#                75% of work done with Pandas is dat cleaning

df = pd.read_json("example-data/mifania_student_data.json")

# 1. Drop irrelevant columns
# df = df.drop(columns=["First_Name", "Last_Name"])


# 2. Handle Missing Data
# df = df.dropna(subset=["Course"]) #Drop the rows with N/A within the defined subset i.e Course
# df = df.fillna({"Course": "N/A"}) #Replace a null value with a customized one

# 3. Fix Inconsistent Values
# df["Gender"] = df["Gender"].replace({"Male": "MALE"}) #Replace small (Male) with all capital (MALE)
# df["Gender"] = df["Gender"].replace( #Multiple replaces
#     {
#         "Male": "MALE",
#         "Female": "FEMALE"
#     }
# ) 

# 4. Standard Text
# df["First_Name"] = df["First_Name"].str.lower()
# df["Last_Name"] = df["Last_Name"].str.lower()

# 5. Fix Data Type
# df["Gender"] = df["Gender"].astype(bool)

# 6. Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())