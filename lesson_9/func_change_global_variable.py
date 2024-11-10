count = 0
def increment():
    global count
    count += 1
increment()
print(f"count = {count}")  # Вывод: count = 1