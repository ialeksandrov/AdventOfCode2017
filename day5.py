# -*- coding: utf-8 -*-
contents = open('day5.txt').read().strip()
rows = contents.split('\n')


def part1():
    instructions = []
    for row in rows:
        instructions.append(int(row))

    index = 0
    step = 0
    while True:
        value = instructions[index]
        instructions[index] += 1
        index += value
        step += 1
        if index < 0 or index >= len(instructions):
            return step

def part2():
    instructions = []
    for row in rows:
        instructions.append(int(row))

    index = 0
    step = 0
    while True:
        value = instructions[index]
        if value >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1
        index += value
        step += 1
        if index < 0 or index >= len(instructions):
            return step


print(part1())
print(part2())

