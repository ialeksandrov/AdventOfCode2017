# -*- coding: utf-8 -*-
with open('day9.txt') as infile:
    line = infile.readline()

    i = 0
    paren_stack = []
    is_garbage = False
    score = 0
    g_count = 0
    while i < len(line):
        ch = line[i]

        if is_garbage:
            if ch == "!":
                i += 2
                continue
            elif ch == ">":
                is_garbage = False
            else:
                g_count += 1
        else:
            if ch == "{":
                paren_stack.append(ch)
            elif ch == "<":
                is_garbage = True
            elif ch == "}":
                score += len(paren_stack)
                paren_stack = paren_stack[:-1]
        i += 1
    print score
    print g_count
