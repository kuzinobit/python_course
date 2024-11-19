# Функция, принимающая произвольное количество аргументов
def average(*args):
    return sum(args) / len(args)
print(average(1, 2, 3))       # 2.0
print(average(4, 5, 6, 7, 8)) # 6.0