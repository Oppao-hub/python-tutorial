def example5(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    last = example5(n - 1)
    second_last = example5(n - 2)
    return last + second_last

fib = example5(10)
print(fib)

# O(2ⁿ)
#How many times the function run multiplied by number of operations inside the fumction