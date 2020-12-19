#!/usr/bin/env python

from aoc import get_input # AoC
import re
from functools import lru_cache
from copy import deepcopy as copy

data = get_input(19)

rules = data.split("\n\n")[0].split("\n")
messages = data.split("\n\n")[1].split("\n")


rulePrim = dict()

for i, rule in enumerate(rules): # make a dict for the rules
    index, val = re.split(r": ", rule)

    rulePrim[int(index)] = val.replace('"', "")


@lru_cache
def containsPointers(ruleStr): # function to check if a rule contains a pointer
    return any(char.isnumeric() for char in ruleStr)

@lru_cache
def getPointersAtPos(string, starti=0):
    thing = set(re.findall( r"\d+", string[starti:] ))

    return thing

from sys import setrecursionlimit
setrecursionlimit(20000)

@lru_cache
def genRegex(rule, loop=False, i=0):
    cont = rulePrim[rule]
    cont = cont.split(" ")

    reg = "("
    for char in cont:
        ispointer = char.isnumeric()
        if( ispointer ):
            if( i < 498 ):
                reg += genRegex(int(char), loop, i+1)
            else:
                reg += "(\w+)"
        else:
            reg += char
    reg += ")"

    return reg

def removeSpaces(rule):
    # remove spaces because they are evil
    cont = rulePrim[rule]
    rulePrim[rule] = cont.replace(" ", "")
    rulePrim[rule] = "^" + rulePrim[rule] + "$"

    return rulePrim[rule]

# go through all messages and check
def part1(rulePrim, messages):
    count = 0
    mesLen = len(messages)
    for i, message in enumerate(messages):
        check = re.match(rulePrim[0], message)
        if(check):
            count += 1
            print(message)

    print("Part1:", count)




rulePrim[8] = "42 | 42 8"
rulePrim[11] = "42 31 | 42 11 31"


rulePrim[8] = genRegex(8)
rulePrim[11] = genRegex(11)

# rulePrim[0] = genRegex(0)
# rulePrim[0] = removeSpaces(0)
# part1(rulePrim, messages)


# rulePrim[8] = "42 | 42 ([a-b]+)"
# rulePrim[11] = "42 31 | 42 ([a-b]+) 31"




rulePrim[0] = genRegex(0)
print("reg done")
rulePrim[0] = removeSpaces(0)
part1(rulePrim, messages)
