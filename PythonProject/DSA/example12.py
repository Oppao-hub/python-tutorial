def example12(n):
    if n == 1:
        return 1
    
    total = 0

    for _ in range(n):
        total += example12(n - 1)

    return total

print(example12(2))

# O(n!)