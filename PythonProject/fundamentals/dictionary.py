# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

if capitals.get("Japan"):
    print("The capital does not exist.")
else:
    print("The capital exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"China": "Hongkong"})
print(capitals)

capitals.popitem()
print(capitals)

# capitals.clear()
print(capitals)

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)

items = capitals.items()
print(items)

for key, value in items:
    print(f"{key}: {value}")