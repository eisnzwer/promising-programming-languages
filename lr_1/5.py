import random

A = []

for _ in range(75):
    A.append(random.uniform(-5,40))

Y = [x for x in A if x < 20]

print("Массив А:")
print(A)
print("\nМассив Y:")
print(Y)
