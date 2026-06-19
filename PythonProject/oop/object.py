# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model} car.")
    
    def stop(self):
        print(f"You stop the {self.model} car")

    def describe(self):
        print(f"This is a {self.color} {self.model} from {self.year}.")

car1 = Car("Mustang", 2026, "Red", False)

car1.describe()
car1.drive()
car1.stop()