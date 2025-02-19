try:
    file = open("data.txt", "r")
    # Работа с файлом
finally:
    print("Этот блок кода выполнится даже при наличии ошибки")