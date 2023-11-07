import multiprocessing

def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    data_arrays = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 20, 30, 40, 50, 60, 70, 80, 90],
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    ]

    pool = multiprocessing.Pool()

    results = pool.map(count_even_numbers, data_arrays)

    pool.close()
    pool.join()

    for i, count in enumerate(results):
        print(f"Массив {i + 1}: {count} четных значений")
