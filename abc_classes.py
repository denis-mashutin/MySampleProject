from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def talk(self):
        pass


class Beast(ABC):

    def eat(self):
        raise NotImplementedError


class Dog(Animal):

    def talk(self):
        print("I say 'WOOF'.")


class Cat(Animal):

    pass


class Human(Animal):

    pass


class Cow(Beast):

    pass
