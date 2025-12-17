from abc import ABC, abstractmethod


# абтрактный класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        pass

    def test2(self):
        print("test2")

class Dog(Animal):
    def make_sound(self):
        print("гав гав")

    def test(self):
        print("test test")

class Cat(Animal):
    def make_sound(self):
        print("мяяяяяу")

puppy = Dog()
puppy.make_sound()

# ощибка, потому что у Cat есть не все нужные методы
kitten = Cat()
kitten.make_sound()