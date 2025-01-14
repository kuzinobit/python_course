person = {"имя": "Иван", "город": "Москва", "профессия": "Инженер"}

# Перебор ключей
for key in person.keys():
    print(key)

# Перебор значений
for value in person.values():
    print(value)

# Перебор пар ключ-значение
for key, value in person.items():
    print(f"{key}: {value}")