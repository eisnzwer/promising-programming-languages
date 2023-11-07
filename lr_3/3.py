class Car:
    def __init__(self):
        self.brand = ""
        self.number = ""
        self.speed = 0

    def enter(self):
        self.brand = input("Введите марку машины: ")
        self.number = input("Введите номер машины: ")

        while True:
            speed_input = input("Введите скорость машины (в числовом формате или словами): ")
            try:
                self.speed = int(speed_input)
                break
            except ValueError:
                words_to_numbers = {
                    "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
                    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10
                }
                if speed_input.lower() in words_to_numbers:
                    self.speed = words_to_numbers[speed_input.lower()]
                    break
                else:
                    print("Неверный формат ввода. Попробуйте еще раз.")


car = Car()
car.enter()

print(f"Марка машины: {car.brand}")
print(f"Номер машины: {car.number}")
print(f"Скорость машины: {car.speed}")
