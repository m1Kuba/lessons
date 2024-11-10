from main import Hero

class MyHero(Hero):
    def __init__(self, name, health=100, power=10, energy=50):
        super().__init__(name, health, power)
        self.energy = energy

    def special_ability(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} использует специальное умение! Осталось энергии: {self.energy}.")
        else:
            print(f"{self.name} недостаточно энергии для специального умения.")

    def action(self):
        super().action()
        self.special_ability()


# Создаем объект класса MyHero и вызываем методы
if __name__ == "__main__":
    hero = MyHero("Супергерой", health=120, power=15, energy=30)
    hero.action()
