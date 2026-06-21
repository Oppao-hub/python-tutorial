menu = {
    "pizza": 50,
    "hotdog": 40,
    "burger": 100,
    "popcorn": 50,
    "soda": 20,
    "lemonade": 20,
}

cart = []
total = 0

print("----------------MENU----------------")
for key, value in menu.items():
    print(f"{key}: ₱{value:.2f}")
print("-------------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower().strip()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not in the menu!")

print("------------YOUR ORDER------------")
for food in cart:
    i = 1
    total = total + menu.get(food)
    print(f"{i}. {food}")

print()
print(f"Total is: ₱{total:.2f}")