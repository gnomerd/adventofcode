#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex

rules = get_input(7).splitlines()

print(rules)


colorRules = dict()

for rule in rules:
    ops = rule.split( " bags contain " )
    contains = ops[1].split(", ")
    color = ops[0]

    colorRules[color] = contains


target = "shiny gold"

nobags = "no other bags."

def parseColor(color):
    contains = colorRules[color]
    containsNum = dict()

    count = 0

    if( len(contains) > 0 ):
        for cont in contains:
            if( cont != nobags ):
                amount, col1, col2 = re.match("^([0-9]+) ([a-zA-Z]+) ([a-zA-Z]+)", cont).groups()
                col = col1 + " " + col2

                containsNum[col] = int(amount)
            else:
                continue

    return containsNum



print("\n")
def getLeastOne(color, count=0):
    cont = parseColor(color)
    out = 0

    try:
        am = cont[target]
        print("##", color, cont, "RET 1\n")
        if(am > 0):
            return 1
    except:
        for col, amount in cont.items():
            print(f"#### {col} |", color, cont, "next")
            out = getLeastOne(col)
            if( out == 1 ):
                break


        return out



def getBagList(color):
    contents = parseColor(color)
    bag = [color]

    if(len(contents) > 0):
        for clr, amount in contents.items():
            bag += [getBagList(clr)] * amount

    return bag



bags = getBagList(target)

def getAmountAllThing(bags):
    count = 0
    for bag in bags:
        if type(bag) == list:
            count += getAmountAllThing(bag)
        else:
            count += 1
    return count

print(getAmountAllThing(bags)- 1)
