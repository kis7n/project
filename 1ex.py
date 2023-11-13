# Пользователь вводит свое имя и возраст
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
# Определяем стаж программирования
if age >= 15:
    # Считаем стаж с 9 класса
    programming_experience = age - 14
else:
    programming_experience = 0
# Проверяем, учится ли человек
if age >= 7 and age <= 17:
    # Определяем класс, в котором учится человек
    grande = age - 6
# Выводим приветственное сообщение с данными пользователя
    print(f"Hello, {name}! You are at {grande} grande and have {programming_experience} years of programming experience. Sounds cool!")
elif age >= 18 and age <= 21:
    # Определяем курс, на котором учится человек в университете
    course = age - 17
# Выводим приветственное сообщение с данными пользователя
    print(f"Hello, {name}! You are at {course} course and have {programming_experience} years of programming experience. Sounds cool!")
else:
    # Человек считается "entrepreneur", если нигде не учится
    course = "entrepreneur"
    print(f"Hello, {name}! You are entrepreneur and have {programming_experience} years of programming experience. Sounds cool!")
    