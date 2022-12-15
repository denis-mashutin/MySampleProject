from classes import Animal


class Horse(Animal):
    food = "grass"
    def animal_food(self):
        print(f"The horse eats {self.food}.")


class Bear(Animal):
    food = "honey"
    def animal_food(self):
        print(f"The bear eats {self.food}.")


class Dog(Animal):
    food = "meat"
    def animal_food(self):
        print(f"The dog eats {self.food}.")