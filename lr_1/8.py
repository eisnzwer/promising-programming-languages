import math

N = int(input("Введите натуральное число N: "))

total_sum = 0

for k in range(1, N+1):
    ln_value = math.log(abs(k / (1+k)))
    k_square = k ** 2
    total_sum += ln_value * k_square

print(total_sum)