# Вложенные словари
students = {
    "student1": {
        "name": "Иван",
        "age": 20,
        "grades": [5, 4, 5]
    },
    "student2": {
        "name": "Мария",
        "age": 22,
        "grades": [5, 5, 5]
    }
}

# Доступ к вложенным данным
print(students["student1"]["name"])     # Иван
print(students["student2"]["grades"])   # [5, 5, 5]