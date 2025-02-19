def check_score(score):
    if score < 0:
        raise ValueError("Отрицательное число не может быть счётом!")
    elif score > 100:
        raise ValueError("Счёт не может превышать 100!")
    else:
        print("Счёт в норме:", score)

try:
    check_score(-10)
except ValueError as e:
    print(f"Ошибка: {e}")