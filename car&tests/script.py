import sys
from car import Car


s = int(sys.argv[1])

car = Car(s)
car.brake()
print(f"Car's current speed is {car.speed}")






