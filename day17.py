# -*- coding: utf-8 -*-
from collections import deque

step = 303
spinlock = deque([0])

for i in range(1, 50000001):
    spinlock.rotate(-step)
    spinlock.append(i)

print(spinlock[spinlock.index(0) + 1])

step = 303

# part 1
i = 0
buf = [0]
for t in range(1, 2017 + 1):
    i = (i+step) % len(buf) + 1
    buf[i:i] = [t] # equivalent to insert
print(buf[i -5:i+5])