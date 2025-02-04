from collections import deque

d = deque([1, 2, 3])

#append(x)
d.append(4)
print(d)  # deque([1, 2, 3, 4])

#appendleft(x)
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4])