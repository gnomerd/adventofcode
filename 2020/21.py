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

#print(len(allfood))

ignorefoods = set( [food for food in allfood] )

seenaller = set()
seenfood = set()

thing = dict()

for i, food in enumerate(foodlist):
    aller = allerlist[i]
    # why is there no NAND? :(

    for j, food2 in enumerate(foodlist):
        if(i == j):
            continue

        aller2 = allerlist[j]
        commonaller = set(aller) & set(aller2)

        commonfood = set(food) & set(food2)

        for ignore in ignorefoods:
            commonfood.discard(ignore)

        for seen in seenfood:
            commonfood.discard(seen)

        for al in commonaller:
            if(al in seenaller):
                continue

            cfList = list(commonfood)
            caList = list(commonaller)
            #breakpoint()
            if( len(commonfood) == 1 and len(commonaller) == 1 ):


                thing[cfList[0]] = caList[0]
                seenfood.add(cfList[0])
                seenaller.add(caList[0])

print(thing)
