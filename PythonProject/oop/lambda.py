# Lambda function = A small anonymous function for a one time use (throw away function)
#                   They take any number of arguments, but have only 1 expression
#                   Help keep the namespace clean and is useful with higher order functions
#                   'sort()', 'map()', 'filter()', 'reduce()'
#                   lambda parameteres: expressin

double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
full_name = lambda first, last: f"{first} {last}"
is_even = lambda x: x % 2 == 0
age_check = lambda age: "Adult" if age >= 18 else "Minor"

print(double(2))
print(add(2, 3))
print(max_value(4, 5))
print(min_value(4, 5))
print(full_name("Spongebob", "Squarepants"))
print(is_even(5))
print(age_check(16))
print(age_check(18))