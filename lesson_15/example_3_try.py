class InvalidPasswordError(Exception):
    pass
def login(password):
    if password != "secret":
        raise InvalidPasswordError("Неверный пароль!")
    print("Успешный вход в систему")

try:
    login("wrong")
except InvalidPasswordError as e:
    print(f"Ошибка: {e}")