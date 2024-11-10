def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(7))   # Вывод: True
print(is_prime(10))  # Вывод: False