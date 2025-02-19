try:
    value = int(input("Введите число: "))
    result = 100 / value
    print(result)
except ValueError:
    print("Ошибка: вы ввели не число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль недопустимо!")