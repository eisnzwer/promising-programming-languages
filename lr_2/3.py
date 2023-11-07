data = [1, 2, 0, 3, 43, 0]
mean = sum(data) / len(data)
data = [it if it else mean for it in data]
print(data)