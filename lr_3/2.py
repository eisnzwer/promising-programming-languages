from abc import ABC, abstractmethod

class FibonacciFinder(ABC):
    @abstractmethod
    def find_fibonacci(self, sequence):
        pass

class FibonacciInSeries(FibonacciFinder):
    def find_fibonacci(self, sequence):
        fibonacci_numbers = []
        a, b = 0, 1
        while b <= max(sequence):
            if b in sequence:
                fibonacci_numbers.append(b)
            a, b = b, a + b
        return fibonacci_numbers

def get_user_input():
    try:
        series = input("Введите ряд чисел через пробел: ").split()
        series = [int(num) for num in series]
        return series
    except ValueError:
        print("Пожалуйста, введите целые числа.")
        return get_user_input()

user_series = get_user_input()
finder = FibonacciInSeries()

fibonacci_numbers = finder.find_fibonacci(user_series)
print("Числа Фибоначчи в ряду:", fibonacci_numbers)
