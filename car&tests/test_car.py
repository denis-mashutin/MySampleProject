from unittest import TestCase

from car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car(30)

    def test_accelerate(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 35)

    def test_brake(self):
        self.car.brake()
        self.assertEqual(self.car.speed, 25)

    def test_accelerate_brake(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 35)
        self.car.brake()
        self.assertEqual(self.car.speed, 25)


class TestSpeeds(TestCase):
    def test_move(self):
        for s in range(0, 101):
            with self.subTest(f"Braking from speed {s}"):
                self.car = Car(s)
                self.car.brake()
                distance = self.car.speed*1
                self.assertTrue(distance >= 0)
