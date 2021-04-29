#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = abs(int(input("Введите целое положительное число ")))
maxnumber = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > maxnumber:
        maxnumber = n % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра в числе ", maxnumber)
        break