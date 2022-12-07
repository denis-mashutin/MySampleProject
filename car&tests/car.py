class Car:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        # self.speed -= 5
        if self.speed <= 5:
            self.speed = 0
        else:
            self.speed -= 5


my_car = Car()
my_car.accelerate()
i = 0
while my_car.speed > 0:
    my_car.brake()
    i += 1
print(f"Car braked {i} times before it stopped")
