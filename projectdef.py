def task1():
    #ex1
        def print_pascal_triangle(n):
            if n < 0:
                print("Ошибка: введите число больше или равное нулю")
                return
            for line in range(n):
                for i in range(line + 1):
                    print(binomial_coefficient(line, i), " ", end="")
                print()
        
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        
        def binomial_coefficient(n, k):
            return int(factorial(n) / (factorial(k) * factorial(n - k)))
        
        n = int(input("Введите целое число: "))
        print_pascal_triangle(n)

def task2():
    #ex2
    def longest_palindrome(s):
        longest = ""
        for i in range(len(s)):                                                             #рассмотрим цикл
            for j in range(i, len(s)):
                substring = s[i:j+1]                                                        #ищем подстроку
                if substring == substring[::-1] and len(substring) > len(longest):          #проверяем полиндром и нахходим макс длину  
                    longest = substring
        return longest
    
    s = input("Пожалуйста, введите строку: ")                                               #пользователю предлагается ввести строку
    result = longest_palindrome(s)                                                          
    if result:
        print("Самая длинная палиндромная подстрока в строке:", result)
    else:
        print("В строке нет палиндромных подстрок.")                                        #учитываем,что полиндрома может и не быть вовсе

def task3():
    #ex3
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

def task4():
    row1 = int(input("введите количество строк первой матрицы: "))
    col1 = int(input("введите количество столбцов первой матрицы: "))
    row2 = int(input("введите количество строк второй матрицы: "))
    col2 = int(input("введите количество столбцов второй матрицы: "))
    if col1 != row2:
        print("умножение невозможно!")
        exit()

# ввод элементов первой матрицы
    a = [[0] * col1 for _ in range(row1)]
    print("введите элементы первой матрицы")
    for i in range(row1):
        for j in range(col1):
            print(f"a[{i}][{j}]= ", end='')
            a[i][j] = float(input())

# вывод элементов первой матрицы
    for i in range(row1):
        for j in range(col1):
            print(a[i][j], end=' ')
        print()


# ввод элементов второй матрицы
    b = [[0] * col2 for _ in range(row2)]
    print("введите элементы второй матрицы")
    for i in range(row2):
        for j in range(col2):
            print(f"b[{i}][{j}]= ", end='')
            b[i][j] = float(input())

# вывод элементов второй матрицы
    for i in range(row2):
        for j in range(col2):
            print(b[i][j], end=' ')
        print()

# умножение матриц
    c = [[0] * col2 for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                c[i][j] += a[i][k] * b[k][j]

# вывод матрицы произведения
    print("матрица произведения")
    for i in range(row1):
        for j in range(col2):
            print(c[i][j], end=' ')
        print()


n = int(input("введите номер задания, которое хотите проверить или 0, если хотите завершить проверку: "))
while True:
    if n == 1:
        task1()
        n = int(input("введите номер задания, которое хотите проверить или 0, если хотите завершить проверку: "))
    elif n == 2:
        task2()
        n = int(input("введите номер задания, которое хотите проверить или 0, если хотите завершить проверку: "))
    elif n == 3:
        task3()
        n = int(input("введите номер задания, которое хотите проверить или 0, если хотите завершить проверку: "))
    elif n == 4:
        task4()
        n = int(input("введите номер задания, которое хотите проверить или 0, если хотите завершить проверку: "))
    elif n == 0:
        break
    else:
        n = int(input('что-то пошло не так, давайте ещё раз: '))
