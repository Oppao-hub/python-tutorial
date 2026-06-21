height = int(input("Height: "))
width = (height * 2) - 1
symbol = input("Enter the symbol to use: ")

for x in range(1, height + 1):
    symbols = symbol * ((x *2) - 1)
    print(f"{symbols:^{width}}")
