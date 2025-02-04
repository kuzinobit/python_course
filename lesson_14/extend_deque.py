from collections import deque

d = deque([1, 2, 3])

#extend(iterable)
d.extend([4, 5])
print(d)  # deque([1, 2, 3, 4, 5])

#extendleft(iterable)
d.extendleft([0, -1])
print(d)  # deque([-1, 0, 1, 2, 3, 4, 5])