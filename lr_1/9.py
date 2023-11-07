import random

N = 14
M = 14

B = [[random.randint(1,100) for _ in range(M)] for _ in range(N)]

D = [0] * M

for j in range(M):
    for i in range(N):
        D[j] += B[i][j]

print("Матрица B:")
for row in B:
    print(row)

print("\n Массив D с суммами столбцов:")
print(D)