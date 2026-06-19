# List Comprehension = a concise way to create list in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]


doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

numbers = [1, -2 ,3 -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]

print(doubles)
print(triples)
print(squares)
print(fruits)
print(fruit_chars)
print(positive_nums)
print(negative_nums)