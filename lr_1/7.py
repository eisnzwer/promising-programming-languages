text = input("Введите текст: ")

words = text.lower().split()

count_no = words.count("no")

print("Ответ:")
print(count_no)
