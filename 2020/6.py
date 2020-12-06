#!/usr/bin/env python

from aoc import get_input
import re

groups = get_input(6).split("\n\n")

def toList(string):
    list = []
    list[:0] = string
    return list

print(groups)

def countQuestions( group ):
    persons = group.split("\n")

    groupQs = []

    for person in persons:
        chars = toList(person)
        for char in chars:
            if(not char in groupQs):
                groupQs.append(char)

    return len(groupQs)


grpCountList = []
grpCount = 0


# 2
def countQuestionsAll( group ):
    persons = group.split("\n")
    personsLen = 0

    groupQs = []

    for person in persons:
        if( person != "" and person != None ):
            personsLen += 1
            chars = toList(person)
            for char in chars:
                if( char and char != "" ):
                    groupQs.append(char)


    allQs = 0
    seenQ = []
    for q in groupQs:
        num = groupQs.count(q)
        if(num == personsLen and not q in seenQ):
            seenQ.append(q)
            allQs += 1

    print(allQs)

    return allQs


grpAllList = []
grpAll = 0

for group in groups:
    num = countQuestions(group)
    grpCount += num
    grpCountList.append( countQuestions(group) )

    num2 = countQuestionsAll(group)
    grpAll += num2
    grpAllList.append(num2)

print("----")
print("Part1:", grpCount)
print("Part2:", grpAll)
