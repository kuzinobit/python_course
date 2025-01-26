fs = frozenset([1, 2, 3])
print(fs)  #
frozenset({1, 2, 3})
fs.add(4)  # Ошибка, так как frozenset неизменяемый