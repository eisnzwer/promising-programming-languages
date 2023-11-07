import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(1, 101, (5, 5))

matrix *= 10

determinant_before = np.linalg.det(matrix)

inverse_matrix = np.linalg.inv(matrix)

determinant_after = np.linalg.det(inverse_matrix)

labels = ['Детерминант до', 'Детерминант после']
values = [determinant_before, determinant_after]

plt.bar(labels, values, color=['blue', 'green'])
plt.ylabel('Значение определителя')
plt.title('Сравнение определителей')
plt.show()
