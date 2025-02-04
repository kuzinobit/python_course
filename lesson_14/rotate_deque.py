from collections import deque

d = deque([1, 2, 3, 4, 5])
d.rotate(2)
print(d)  # deque([4, 5, 1, 2, 3])
d.rotate(-3)
print(d)  # deque([2, 3, 4, 5, 1])