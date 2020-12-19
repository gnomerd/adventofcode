#!/usr/bin/env python

from aoc import get_input # AoC
import re
from functools import lru_cache

data = get_input(19)

rules = data.split("\n\n")[0].split("\n")
messages = data.split("\n\n")[1].split("\n")


rulePrim = dict()

for i, rule in enumerate(rules): # make a dict for the rules
    index, val = re.split(r": ", rule)

    rulePrim[int(index)] = val.replace('"', "")

#print(rulePrim)

@lru_cache
def containsPointers(ruleStr): # function to check if a rule contains a pointer
    return any(char.isnumeric() for char in ruleStr)

@lru_cache
def getPointersAtPos(string, starti=0):
    thing = set(re.findall( r"\d+", string[starti:] ))

    return thing

# @lru_cache
# def genRegex(rule, newrule=None, pointers=None):
#     #for rule, cont in rulePrim.items(): # replace everything with the chars instead of pointers
#     #print("New rec")
#     newrule = newrule or rulePrim[rule]
#     print("NEW REC")

#     pointers = pointers or getPointersAtPos(newrule)

#     for i, pointer in enumerate(pointers):
#         pointsTo = rulePrim[int(pointer)]
#         repl = f"({rulePrim[int(pointer)]})"

#         #print(f"Checking pointer {i}/{len(pointers)-1}", end="\r")
#         newrule = newrule.replace(str(pointer), repl)

#     #print("")
#     check = getPointersAtPos(newrule)
#     if(len(check) > 0):
#         return genRegex(rule, newrule)
#     else:
#         return newrule

@lru_cache
def genRegex(rule):
    cont = rulePrim[rule]
    cont = cont.split(" ")

    reg = "("
    for char in cont:
        ispointer = char.isnumeric()
        if( ispointer ):
            reg += genRegex(int(char))
        else:
            reg += char
    reg += ")"

    return reg


    
def removeSpaces(rule):
    # remove spaces because they are evil
    cont = rulePrim[rule]
    print("########################", cont)
    rulePrim[rule] = cont.replace(" ", "")
    rulePrim[rule] = "^" + rulePrim[rule] + "$"

    return rulePrim[rule]


# go through all messages and check
def part1(rulePrim, messages):
    count = 0
    mesLen = len(messages)
    for i, message in enumerate(messages):
        check = re.match(rulePrim[0], message)
        print(f"Checking {message} [{i}/{mesLen}]")
        if(check):
            print("is valid")
            count += 1

    print("Part1:", count)



rulePrim[8] = "42 | 42 8"
rulePrim[11] = "42 31 | 42 11 31"
rulePrim[0] = genRegex(0)
print(rulePrim[0])


rulePrim[0] = removeSpaces(0)
part1(rulePrim, messages)
