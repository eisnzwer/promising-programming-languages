import threading

m, n, k = 3, 3, 3

matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matrix_C = [[0 for _ in range(k)] for _ in range(m)]

lock = threading.Lock()

def calculate_element(i, j):
    global matrix_C

    import time
    time.sleep(1)

    result = 0
    for x in range(n):
        result += matrix_A[i][x] * matrix_B[x][j]

    with lock:
        matrix_C[i][j] = result

def main():
    threads = []

    for i in range(m):
        for j in range(k):
            thread = threading.Thread(target=calculate_element, args=(i, j))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

    for row in matrix_C:
        print(row)

if __name__ == "__main__":
    main()

