from abc import ABC, abstractmethod
import random

class Pet(ABC):
    def __init__(self, name, satiety):
        self.name = name
        self.satiety = satiety

    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        print(self.sound())
        self.satiety += 75
        if self.satiety > 100:
            self.satiety = 100

class Dog(Pet):
    def sound(self):
        return "Гав!"

class Cat(Pet):
    def sound(self):
        return "Мяу!"

pets = []
for _ in range(5):
    name = "Питомец" + str(_)
    satiety = random.randint(1, 100)
    pet_type = random.choice([Dog, Cat])
    pets.append(pet_type(name, satiety))

print("Состояние питомцев до кормления:")
for pet in pets:
    print(f"{pet.name}: Сытость - {pet.satiety}%")

for pet in pets:
    pet.eat()

print("\nСостояние питомцев после кормления:")
for pet in pets:
    print(f"{pet.name}: Сытость - {pet.satiety}%")
