# recursion = a function that calls itself from within
#             help to visualize a complex problem in to basic steps,
#             which can be solve more easily iteratively or recursively

#ITERATIVE
# def walk(steps):
#     for step in range(1, steps +1):
#         print(f"You take step #{step}")

def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"You take step #{steps}")

#walk(100)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
print(factorial(5))