def func():
    x = 10  # Локальная переменная
    print(f"Внутри функции: x = {x}")
func()
print(f"Вне функции: x = {x}")  # Ошибка: x не определен