person = {"name": "Иван", "age": 30}

# Использование setdefault()
value = person.setdefault("salary", 50000)
print(value)       # 50000
print(person)