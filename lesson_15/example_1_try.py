def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Файл не найден.")
    except PermissionError:
        print("Недостаточно прав для чтения файла.")

content = read_file("data.txt")
if content is not None:
    print("Содержимое файла:", content)