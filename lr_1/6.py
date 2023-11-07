import numpy as np

X = np.random.rand(15,20)
Y = np.random.rand(15)

np.set_printoptions(precision=2, suppress=True, linewidth=150)
print("Исходная матрица X:")
print(X)

for i in range(20):
    if i % 2 == 0:
        X[:, i] = Y

print("\nОбновленная матрица X:")
print(X)