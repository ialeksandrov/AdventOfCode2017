# -*- coding: utf-8 -*-
my_input = 361527

total, level = 1, 1

while total < my_input:
    level += 2
    total = total + level*4 - 4 # or the easy (not my) way: total = level ** 2

offset = total - my_input
steps = offset % (level - 1)

print (level - 1) / 2 + abs((level / 2) - steps)