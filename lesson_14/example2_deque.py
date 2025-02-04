from collections import deque

buffer = deque(maxlen=3)
buffer.append(1)
buffer.append(2)
buffer.append(3)
print(buffer)  # deque([1, 2, 3], maxlen=3)
buffer.append(4)
print(buffer)  # deque([2, 3, 4], maxlen=3) - элемент 1 был удалён