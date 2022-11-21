class Dog:

    is_domestic = True
    sound = 'WOOF!'

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"I say {self.sound}")


class Cat:

    is_domestic = True
    sound = 'MEOW!'

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"I say {self.sound}")


class A:

    def __init__(self, a):
        self.a = a
