from collections import deque

tasks = deque()

# Добавляем задачи в очередь tasks.append("task1")
tasks.append("task2")
tasks.append("task3")

# Обработка задач в порядке FIFO while tasks:
current_task = tasks.popleft()
print(f"Выполняется: {current_task}")