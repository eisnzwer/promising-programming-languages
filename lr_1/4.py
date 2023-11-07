import random

A1 = []

for _ in range(75):
    A1.append(random.uniform(16,53))

A2 = [x for x in A1 if 25.8 < x < 34.7]

print("Массив А1:")
print(A1)
print("\nМассив А2:")
print(A2)
