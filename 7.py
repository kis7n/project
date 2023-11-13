# Ввод последовательности чисел
sequence = input('Введите последовательность чисел: ').split()
# Максимальное количество подряд идущих чисел равных друг другу
max_count = 1
# Число, которое повторяется максимальное количество раз
max_number = sequence[0]

# Подсчет количества повторяющихся чисел
current_count = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i-1]:
        current_count += 1
        if current_count > max_count:
            max_number = sequence[i]
            max_count = current_count
    else:
        current_count = 1

# Вывод результата
print(f'Наибольшее количество подряд идущих чисел равных друг другу: {max_count}')
print(f'Число, которое повторяется максимальное количество раз: {max_number}')
