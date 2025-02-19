try:
    # Код, в котором возможна ошибка
    result = 10 / 0
except ZeroDivisionError:
    # Обработка ошибки
    print("Деление на ноль невозможно!")