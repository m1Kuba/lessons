from abc import ABC, abstractmethod

# Абстрактный класс Room
class Room(ABC):
    def __init__(self, features, price):
        self._features = features
        self.__price = price

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_features(self):
        pass

# Класс StandardRoom
class StandardRoom(Room):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features

# Класс LuxuryRoom с WiFi и завтраком
class WiFiService:
    def get_wifi_description(self):
        return "Wi-Fi доступен в номере."

class BreakfastService:
    def get_breakfast_description(self):
        return "Завтрак включён в стоимость."

class LuxuryRoom(Room, WiFiService, BreakfastService):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features + [self.get_wifi_description(), self.get_breakfast_description()]

# Класс FamilyRoom с WiFi
class FamilyRoom(Room, WiFiService):
    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features + [self.get_wifi_description()]

# Тестирование
standard_room = StandardRoom(features=["Телевизор", "Душ"], price=100)
luxury_room = LuxuryRoom(features=["Телевизор", "Душ", "Кондиционер"], price=200)
family_room = FamilyRoom(features=["Телевизор", "Душ", "Детская кровать"], price=150)

rooms = [standard_room, luxury_room, family_room]

for room in rooms:
    print("Цена:", room.get_price())
    print("Удобства:", room.get_features())
    print()
