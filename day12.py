# -*- coding: utf-8 -*-
import re, itertools

with open("day12.txt") as fp:
    lines = fp.read().strip().splitlines()

related = {p: set(r) for p, *r in (re.findall(r'\d+', l) for l in lines)}

def connected(available):
    explored = set()
    while available:
        explored.update(available)
        available = {y for x in available for y in related[x]} - explored
    return explored

groups = []
while related:
    x = min(related)
    ys = connected({x})
    for y in ys:  del related[y]
    groups.append(ys)

print(len(groups[0]))
print(len(groups))

