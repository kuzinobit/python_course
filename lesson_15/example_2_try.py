def safe_division():
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        return a / b
    except ValueError:
        print("Ошибка ввода: нужно ввести число.")
    except ZeroDivisionError:
        print("Деление на ноль недопустимо.")

result = safe_division()
if result is not None:
    print("Результат:", result)