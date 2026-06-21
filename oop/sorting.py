# SORTING IN PYTHON .sort() or .sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects 

# ---------------LISTS----------------

# fruits = ["banana", "orange", "apple", "coconut"]
# numbers = [ 4, 5, 3, 2, 1]

# numbers.sort(reverse=True)
# fruits.sort(reverse=True)

# print(fruits)
# print(numbers)


# ---------------TUPLES----------------
# fruits = ("banana", "orange", "apple", "coconut")
# numbers = (4, 5, 3, 2, 1)

# fruits = sorted(fruits)
# numbers = sorted(numbers)

# #fruits = sorted(fruits, reverse=True) #Reverse
# #fruits = tuple(fruits) # Typecast to tuple

# print(fruits)
# print(numbers)

# ---------------DICTIONARY----------------
fruits = {
    "banana": 105, 
    "orange": 73,
    "apple": 72,
    "coconut": 354
}

#fruits = dict(sorted(fruits.items()))
#fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True)) #sort by key
fruits = dict(sorted(fruits.items(), key=lambda item: item[1])) #sort by value
# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True)) 
#index 1 will reverse the value and index 0 will reverse the key

print(fruits)