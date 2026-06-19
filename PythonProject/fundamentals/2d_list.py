
groceries = [
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "beef"]
]

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()