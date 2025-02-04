from collections import deque

d = deque([0, 1, 2, 3, 4])

#pop()
last = d.pop()
print(last)  # 4
print(d)      # deque([0, 1, 2, 3])

#popleft()
first = d.popleft()
print(first)  # 0
print(d)       # deque([1, 2, 3])