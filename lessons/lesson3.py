# from datetime import datetime
#
# import time
# Инкапсуляция


# _ это защищен от изменения
# __ это защищен от приватный

# class BankAccountService:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance # _ защищен атрибут, __  приватный атрибут
#
#     def __deposit(self, amount):
#
#         if amount > 0:
#             self._balance += amount
#             return f"Баланс {self.owner} пополнен на {amount}. Текущий баланс: {self.__balance}"
#         else:
#             return "Сумма должна быть положительной."
#
#     def get_balance(self):
#         return f"ваш баланс {self.__balance}"
#
#
# account = BankAccount("Вася", 100)
# # print(account.get_balance())
# print(account._BankAccount__balance) # _ защищен атрибут
# print(dir(account))


# Абстракция
# from abc import ABC, abstractmethod
#
# from lessons.lesson1 import Person
#
#
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Dog(Animal):
#
#     def make_sound(self):
#         return print("ГАв Гав")
#
#     def move(self):
#         return f"Ходит на лапах"
#
# class Cat(Animal):
#
#     def make_sound(self):
#         return print("Мяу Мяу")
#
#     def move(self):
#         return print("Ходит без шумно")
#
# dog = Dog()
# cat = Cat()
#
# dog.make_sound()
# print(dog.move())
#
# cat.move()
# cat.make_sound()


# 3. Множественное наследование

class Animal:
    def make_sound(self):
        return "Издает звук"


class Swimmable:
    def move(self):
        return "Плавает"

class Flyable:
    def move_1(self):
        return "Летит"

#Метод разрешения порядка (MRO): Python использует алгоритм C3-линеаризации для определения порядка,
# в котором методы классов будут вызваны, если они определены в нескольких родительских классах.


class Duck(Animal, Flyable, Swimmable):

    def make_sound(self):
        return  print("Гря Гря")


duck = Duck()

print(duck.move())
duck.make_sound()

print(Duck.__mro__)