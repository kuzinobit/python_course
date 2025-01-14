# Инвертирование словаря
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)  # {1: 'a', 2: 'b', 3: 'c'}