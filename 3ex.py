n, m, k, h = map(int, input().split())

# Создаем матрицу matrix1 размером n x m и заполняем ее значениями, введенными пользователем
matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Создаем матрицу matrix2 размером k x h и заполняем ее значениями, введенными пользователем
matrix2 = []
for _ in range(k):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Создаем матрицу result размером n x h, заполняем ее нулями
result = [[0] * h for _ in range(n)]

# Проходим по каждому элементу матрицы result
for i in range(n):
    for j in range(h):
        sum = 0
        # Умножаем каждый элемент строки i матрицы matrix1
        # на соответствующий элемент столбца j матрицы matrix2
        for idx in range(m):
            sum += matrix1[i][idx] * matrix2[idx][j]
        result[i][j] = sum

# Выводим полученную матрицу result
for row in result:
    print(*row)
