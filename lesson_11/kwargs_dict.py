# Функция с **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Анна", age=25, city="Санкт-Петербург")