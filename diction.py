from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Pet(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Pet):
    def eat(self):
        print("bone")

    def sleep(self):
        print("sleeping....")


dog = Dog()
dog.sleep()
dog.eat()
print(type(Pet))
