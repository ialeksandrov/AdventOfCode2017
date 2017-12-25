# -*- coding: utf-8 -*-
import collections

with open("day8.txt") as fp:
    lines = fp.read().strip().splitlines()

registers = set()
intermediate = set()
for line in lines:
    terms = collections.deque(line.split() + [":"])
    terms.rotate(5)
    v1, v2 = terms[1], terms[-3]
    registers |= {v1, v2}
    locals().setdefault(v1, 0)
    locals().setdefault(v2, 0)
    exec(" ".join(terms).replace("dec", "-=").replace("inc", "+="))
    intermediate.add(eval(v2))
print("Part1: ", max(map(eval, registers)))
print("Part2: ", max(intermediate))
