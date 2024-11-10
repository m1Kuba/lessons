class Hero:
    def __init__(self, name, health=100, power=10):
        self.name = name
        self.health = health
        self.power = power

    def action(self):
        print(f"{self.name} делает базовую атаку с силой {self.power}!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона и теперь имеет {self.health} здоровья.")
