# Использование remove()
fruits = ["яблоко", "банан", "вишня"]
fruits.remove("банан")
print(fruits)  # ["яблоко", "вишня"]
print()

# Использование pop()
fruits = ["яблоко", "банан", "вишня"]
last_fruit = fruits.pop()
print(last_fruit)  # "вишня"
print(fruits)      # ["яблоко"]
print()

# Использование clear()
fruits = ["яблоко", "банан", "вишня"]
fruits.clear()
print(fruits)  # []