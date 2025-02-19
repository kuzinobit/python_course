try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("Файл не найден.")
else:
    content = file.read()
    print("Содержимое файла:", content)
    file.close()