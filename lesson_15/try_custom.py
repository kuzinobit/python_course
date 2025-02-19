class MyCustomError(Exception):
    """Особое исключение для моей программы."""
    pass

def process_value(x):
    if x < 0:
        raise MyCustomError("Значение не может быть отрицательным!")
    return x * 2
try:
    result = process_value(-5)
except MyCustomError as e:
    print(f"Произошла ошибка: {e}")