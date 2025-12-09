class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # ----- Геттеры -----
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # ----- Сеттеры -----
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным.")

    def make_sound(self):
        return "Some generic animal sound"



class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"



dog = Dog("Бобик", 3)
cat = Cat("Мурка", 2)

print(dog.get_name(), "-", dog.make_sound())
print(cat.get_name(), "-", cat.make_sound())

dog.set_name("Шарик")
dog.set_age(5)

cat.set_name("Луна")
cat.set_age(4)

print("\nПосле изменения:")
print(dog.get_name(), dog.get_age())
print(cat.get_name(), cat.get_age())
