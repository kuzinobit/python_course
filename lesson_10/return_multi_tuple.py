# Функция, возвращающая кортеж
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([1, 2, 3, 4, 5])
min_value, max_value = result
print(f"Min: {min_value}, Max: {max_value}")  # Min: 1, Max: 5