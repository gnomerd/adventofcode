#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex:
from itertools import permutations as per
from itertools import combinations as co
from functools import lru_cache


minjolt, maxjolt = 1, 3

jolts = sorted(list(map(int, get_input(10).splitlines())))

jolts.insert(0, 0) # first one is allways 0
jolts.append( max(jolts)+3 ) # my adapter, allways higher than the highest by 3

# used = []

# def getBest(i, jolts):
#     num = jolts[i]

# diffs = []
# for i in range(len(jolts)):

#     if( i > 0 ):
#         bestdiff = jolts[i] - jolts[i-1]
#         diffs.append(bestdiff)

# diff1, diff3 = diffs.count(1), diffs.count(3)
# part1 = diff1 * diff3
# print(part1)


# part 2

def validateJolts(combo, rng):
    valid = True
    for i in range(len(combo)):
        if( i > 0 ):
            num1, num2 = combo[i-1], combo[i]
            if( not (num2 - num1) in rng ):
                valid = False
    return valid


# def getNextJolt(num, diff, jolts):
#     for jolt in jolts:
#         if( jolt != num ):
#             if( jolt - diff == num ):
#                 return jolt


# def genCombo(jolts, i=0, diff=1, newcombo = [0]):
#     # first one is allways 0 and last is allways last+3
#     # sorted list so this works

#     nextjolt = getNextJolt(newcombo[i], diff, jolts)

#     if(nextjolt):
#         newcombo.append(nextjolt)

#         genCombo(jolts, i+1, diff, newcombo)
#     else:
#         return newcombo




# print(genCombo(jolts))

#cache = []

@lru_cache
def countCombos(i, count=0):
    num = jolts[i]

    if( num != max(jolts) ):
        for diff in range(1, 4):
            if((num + diff) in jolts):
                index = jolts.index(num + diff)
                print("####", count, diff, index)
                count += countCombos( index )

        return count

    else:
        print("end")
        return 1

        

count = countCombos(0)
print("####################", count)























# print("gen combos")
# combos = per(jolts)
# print("done")
# print(combos)

# #print("getting len")
# combolen = 2 ** len(jolts)
# #print("done", combolen)

# cache = []

# actual = []
# i = 0
# for combo in combos:
#     if( not combo in cache ):
#         print("Checking", f"{i}/{combolen} actual:{len(actual)}", end="\r" )
#         cache.append(combo)
#         validcheck = validateJolts(combo, range(1, 4))
#         if( validcheck ):
#             actual.append(combo)

#     i += 1

# #test = validateJolts(combos[2], range(1, 4))
# #print(test, combos[2])

# print("")
# print(len(actual))

# # listlen = len(jolts)
# # print(2 ** listlen)
