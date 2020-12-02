#!/usr/bin/env python
from aoc import get_input

#data = get_input(2).splitlines()
#print(data)

inp = open("input.2", "r")
inp = inp.read().splitlines()

def getOper(inp):
    ops = []
    passw = []
    for op in inp:
        ops.append(op.split(":")[0])
        passw.append(op.split(":")[1])
    return ops, passw

def getRng(op):
    x = op.split(" ")
    rng = list( map( int, x[0].split("-") ) )
    char = x[1]

    return rng, char

def countChar(string, char):
    s = 0
    for i in range(len(string)):
        if( string[i] == char ):
            s += 1
    return s

ops, passw = getOper(inp)
validsum = 0

PART 1

for i in range(len(ops)):
    op = getRng(ops[i])
    char = op[1]
    rng = op[0]

    pas = passw[i]

    count = countChar(pas, char)
    if( count >= rng[0] and count <= rng[1] ):
        print("true", pas)
        validsum += 1

print(validsum)

def split(word):
    return [char for char in word]

# PART 2
valid2 = 0
for i in range(len(ops)):
    op = getRng(ops[i])
    char = op[1]
    rng = op[0]

    pas = split(passw[i])
    print(pas)

    r1 = int(rng[0])
    r2 = int(rng[1])
    print("###", r1, r2)
    fch = str(pas[r1])
    sch = str(pas[r2])
    print("###", fch, sch)

    print(pas, "|", fch, sch, op, not fch == sch, fch == char or sch == char)

    if( fch != sch and (fch == char or sch == char) ):
        valid2 += 1
        print("valid")

print(valid2)
