class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"
    
fruits = [
    Fruit("banana", 105),
    Fruit("apple", 72),
    Fruit("orange", 73),
    Fruit("coconut", 354)
]

#fruits = sorted(fruits, key=lambda fruit: fruit.name) #sort by name(key)
#fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True) #Reverse
#fruits = sorted(fruits, key=lambda fruit: fruit.calories) #sort by calories(value)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True) #Reverse


print(fruits)