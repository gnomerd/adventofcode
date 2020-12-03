#!/usr/bin/env python
from aoc import get_input

inp = get_input(3).splitlines()

mapp = inp

def step(startx, starty):
    return startx + 3, starty + 1

def getaround(x, y):
    left = mapp[x-1][y]
    right = mapp[x+1][y]
    return left, right

maplen = len(mapp)

def slope(a, b):
    trees = 0
    x, y = 0, 0

    while True:
        try:
            x += a
            y += b

            if( x >= len(mapp[0]) ):
                x = x - len(mapp[0])

            if( mapp[y][x] == "#" ):
                trees += 1
        except:
            break

    return trees

tree1 = slope(3, 1)
print("1:", tree1)

tree2 = slope(1, 1) * tree1 * slope(5, 1) * slope(7, 1) * slope(1, 2)
print(tree2)
