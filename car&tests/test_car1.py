import pytest
from car import Car

car = Car(30)


def test_accelerate():
    car.accelerate()
    assert car.speed == 35


def test_brake():
    car.brake()
    assert car.speed == 25


speeds = range(0, 101)


@pytest.mark.parametrize("speeds", speeds)
def test_move(speeds):
    car = Car(speeds)
    car.brake()
    distance = car.speed*1
    assert distance >= 0
