#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex
from collections import defaultdict as dd
from copy import deepcopy as copy

data = get_input(21).splitlines()

foodlist = []
allfood = []

allerlist = []

allerthing = dd(set)

for food in data:
    cont, aller = food.split("(")
    cont = cont.strip().split(" ")
    aller = aller.replace(")", "").replace("contains ", "").split(", ")

    foodlist.append(cont)
    allerlist.append(set(aller))

    for c in cont:
        allfood.append(c)


for i, food in enumerate(foodlist):
    aller = allerlist[i]

    for al in aller:
        if( not al in allerthing.keys() ):
            allerthing[al] = set(food)
        else:
            allerthing[al] &= set(food)

#print(allerthing)

for aller, cont in allerthing.items():
    for thing in cont:
        while(thing in allfood):
            allfood.remove(thing)

print(len(allfood))

ignorefoods = set( [food for food in allfood] )

seenaller = set()
seenfood = set()

thing = dd(set)

def getFood(foodList, exclude=set()):
    food = set(foodList)
    for ignore in ignorefoods:
        food.discard(ignore)

    for ex in exclude:
        food.discard(exclude)

    return food

takenAllers = set()
for i, food in enumerate(foodlist):
    food = getFood(food)
    aller = allerlist[i]

    if( len(food) == 1 and len(aller) == 1 ):
        if( not list(aller)[0] in takenAllers ):
            thing[list(food)[0]] = list(aller)[0]
            ignorefoods.add(list(food)[0])

    elif(len(food) > 1 and len(aller) > 1):
        for j, food2 in enumerate(foodlist):
            if(i == j):
                continue

            food2 = getFood(food2)
            aller2 = allerlist[j]

            commonFood = list(food & food2)
            commonAller = list(set(aller) & set(aller2))

            for ignore in ignorefoods:
                while(ignore in commonFood):
                    commonFood.remove(ignore)

            for ignore in takenAllers:
                while(ignore in commonAller):
                    commonAller.remove(ignore)

            print(commonFood, commonAller)

            if(len(commonFood) >= 1 and len(commonAller) >= 1):
                if( not commonAller[0] in takenAllers ):
                    thing[commonFood[0]] = commonAller[0]
                    ignorefoods.add(commonFood[0])
                    takenAllers.add(commonAller[0])




print(thing)
sortedthing = sorted(thing.items(), key = lambda kv:(kv[1], kv[0]))
print(sortedthing)

part2 = ""
for i, sort in enumerate(sortedthing):
    part2 += f"{sort[0]}"
    if( i < len(sortedthing)-1 ):
        part2 += ","

print("###########", part2)
