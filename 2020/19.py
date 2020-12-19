#!/usr/bin/env python

from aoc import get_input # AoC
import regex
import re

data = get_input(19)

rules = data.split("\n\n")[0].split("\n")
messages = data.split("\n\n")[1].split("\n")


rulePrim = dict()

for i, rule in enumerate(rules): # make a dict for the rules
    index, val = re.split(r": ", rule)

    rulePrim[int(index)] = val.replace('"', "")

def containsPointers(rule): # function to check if a rule contains a pointer
    cont = rulePrim[rule]

    contains = False
    for char in cont:
        if(char.isnumeric()):
            contains = True
            break

    return contains

for rule, cont in rulePrim.items(): # replace everything with the chars instead of pointers
    check = containsPointers(rule)

    while(check):
        for i in range(len(rulePrim[rule])):
            char = rulePrim[rule][i]

            if(char == " "):
                continue

            if(char.isnumeric()):
                v = int(char)
                pointsTo = rulePrim[v]
                repl = f"{rulePrim[v]}"

                if(len(pointsTo) > 1):
                    repl = f"({rulePrim[v]})"

                rulePrim[rule] = rulePrim[rule].replace(char, repl)

        check = containsPointers(rule)

    #rulePrim[rule] = rulePrim[rule].replace(" ", "")


def findParens(s):
    toret = dict()
    pstack = []

    for i, c in enumerate(s):
        if( c == "(" ):
            pstack.append(i)
        elif( c == ")" ):
            if( len(pstack) == 0 ):
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if(len(pstack) > 0):
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret

def getHighestParen(parens):
    bestkey = None
    bestdiff = None

    for k, v in parens.items():
        diff = v - k
        if(bestdiff == None):
            bestdiff = diff
            bestkey = k
            continue

        if(diff > bestdiff):
            bestdiff = diff
            bestkey = k

    return bestkey


for rule, val in rulePrim.items():
