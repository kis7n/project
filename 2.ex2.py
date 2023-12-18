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
