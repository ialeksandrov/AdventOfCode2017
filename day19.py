# -*- coding: utf-8 -*-
with open('day19.txt') as f:
    instructions = f.readlines()

pos = instructions[0].find('|') + 0j
direction = 1j
letters = []
steps = 0


get_char = lambda pos: instructions[int(pos.imag)][int(pos.real)]

def change_direction(old_direction):
    candidate = old_direction * 1j
    if get_char(pos + candidate) != ' ':
        return candidate
    else:
        return old_direction * -1j


char = get_char(pos)
while char != ' ':
    steps += 1
    if char.isalpha():
        letters.append(char)
    elif char == '+':
        direction = change_direction(direction)
    pos += direction
    char = get_char(pos)

print(''.join(letters))
print(steps)