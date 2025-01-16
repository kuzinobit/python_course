numbers = {1, 2, 3, 4}
numbers.remove(4)
print(numbers)  # {1, 2, 3}
numbers.discard(5)  # не вызовет ошибку, элемент 5 не существует
print(numbers)       # {1, 2, 3}