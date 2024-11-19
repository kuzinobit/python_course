# Распаковка с использованием *
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers
print(a)      # 1
print(b)      # 2
print(rest)   # [3, 4, 5]