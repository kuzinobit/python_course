# Преобразование списка в множество (для удаления дубликатов)
list_of_items = [1, 2, 2, 3, 4, 4, 5]
print(type(list_of_items)) # <class 'list'>
unique_items = set(list_of_items)
print(unique_items)  # {1, 2, 3, 4, 5}
print(type(unique_items)) # <class 'set'>