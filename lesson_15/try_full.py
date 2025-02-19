try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("Файл не найден.")
else:
    data = file.read()
    print("Файл прочитан успешно!")
    file.close()
finally:
    print("Блок finally: выполняется в любом случае.")