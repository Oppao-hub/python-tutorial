import pandas as pd

#Series = A panda 1-Dimensional labeled array that can hold any data type
#         Think of it like a single column in a spreadsheet (1-Dimensional)

# data = [100, 102, 104, 202, 204, 206]

# series = pd.Series(data, index=["a", "b", "c", "e", "f", "g"]) #The index is the labels
# print(series)

# print(series.loc["a"]) #Access a value using the label

# series.loc["b"] = 200 #Set a new value (edit)
# print(series)

# print(series.iloc[2]) #Locate by integer position

# #Filter by values
# print(series[series >= 200])
# print(series[series < 200])

# calories = {
#     "Day 1": 1750, 
#     "Day 2": 2100,
#     "Day 3": 1700
# }

# series = pd.Series(calories)

# series.loc["Day 3"] += 500

# print(series.loc["Day 3"])