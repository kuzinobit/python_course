person = {
    "имя": "Иван",
    "возраст": 30,
    "город": "Москва" }

# Удаление элемента
del person["город"]
print(person)

# Полное удаление словаря
del person
#print(person)  # NameError: name 'person' is not defined