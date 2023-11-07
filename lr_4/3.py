import matplotlib.pyplot as plt

data = [('школа', 10), ('кафе', 20), ('парк', 15), ('магазин', 25)]

types, point_counts = zip(*data)

plt.figure(figsize=(8, 6))
plt.bar(types, point_counts, color='skyblue')
plt.xlabel('Тип места')
plt.ylabel('Количество точек')
plt.title('Количество точек на карте по типам места')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
