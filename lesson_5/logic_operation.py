# Логическое И
result_1 = (5 > 3) and (5 < 10)  # True
result_2 = (5 > 3) and (5 > 10)  # False
print(result_1)
print(result_2)
print()

# Логическое ИЛИ
result_1 = (5 > 3) or (5 > 10)   # True
result_2 = (5 < 3) or (5 > 10)   # False
print(result_1)
print(result_2)
print()

# Логическое НЕ
result_1 = not (5 > 3)  # False
result_2 = not (5 < 3)  # True
print(result_1)
print(result_2)