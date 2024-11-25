# 1 Инкапсуляция
class Person:
    def _init_(self):
        self._age = 0
    def set_age(self, age):
        if age < 0:
            print('Возраст не может быть отрицательным')
        else:
            self._age = age
    def get_age(self):
        return self._age

# 2 Наследование

class Animal:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def speak(self):
        return 'I am an animal'

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())

# 3 Полиморфизм

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))


# 4 Абстракция

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Метод для вычисления площади фигуры."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Вычисление площади прямоугольника."""
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Вычисление площади круга."""
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(f"Площадь прямоугольника: {rect.area()}")
print(f"Площадь круга: {circle.area():.2f}")