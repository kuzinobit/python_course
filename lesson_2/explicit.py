# Явное преобразование

# Преобразование строки в число
age_str = "30"
age_int = int(age_str)
print(age_int) # 30
print(type(age_int)) # <class 'int'>

# Преобразование числа в строку
number = 100
number_str = str(number)
print(number_str) # "100"
print(type(number_str)) # <class 'str'>

# Преобразование числа с плавающей точкой в целое число
pi = 3.1416
pi_int = int(pi)
print(pi_int) # 3
print(type(pi_int)) # <class 'int'>

# Преобразование числа в логическое значение
zero = 0
one = 1
print(bool(zero)) # False
print(bool(one)) # True