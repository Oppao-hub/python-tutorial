def example7(n):
    if n == 0:
        return
    
    print(n)
    example7(round(n/2)) #if n/3 the time complexity will be log₃(n)

# log₂(n)