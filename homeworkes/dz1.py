class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    # 1 задание
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}.")
    # 2 задание
    def is_adult(self):
        return self.age >= 18
    # 3 задание
    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"



person1 = Person("Кубанычбек", 19, "Бишкек")
person2 = Person("Алихан", 14, "Балыкчы")
person3 = Person("Айдана", 21, "Каракол")


print(f"{person1.name} взрослый? {person1.is_adult()}")
print(f"{person2.name} взрослый? {person2.is_adult()}")
print(f"{person3.name} взрослый? {person3.is_adult()}")


print(person1)