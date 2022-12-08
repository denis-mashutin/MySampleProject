import sys
from car import Car

# The value of s in assigned from the first argument
s = int(sys.argv[1])

car = Car(s)
for i in range(2):
    car.brake()
print(f"Car's current speed is {car.speed}")
