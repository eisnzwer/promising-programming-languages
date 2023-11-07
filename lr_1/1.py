m = int(input())

if m <= 0:
    print("Impossible")
else:
    a = int((m // 2) ** .5)
    b = int(m ** 0.5) + 1
    for i in range(a, b):
        j = int((m - i * i) ** .5)
        if i * i + j * j == m:
            print(i, j)
            break
    else:
        print("Impossible")