# -*- coding: utf-8 -*-
with open("day4.txt") as inputData:
    row = [line.split() for line in inputData]

result = 0

for passphrase in row:
    if (len(passphrase) == len(set(["".join(sorted(word)) for word in passphrase]))):
        result += 1

print(result)