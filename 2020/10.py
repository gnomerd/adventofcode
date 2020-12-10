#!/usr/bin/env python

from aoc import get_input # AoC
from functools import lru_cache


minjolt, maxjolt = 1, 3

jolts = sorted(list(map(int, get_input(10).splitlines())))

jolts.insert(0, 0) # first one is allways 0
jolts.append( max(jolts)+3 ) # my adapter, allways higher than the highest by 3

used = []

def getBest(i, jolts):
    num = jolts[i]

diffs = []
for i in range(len(jolts)):

    if( i > 0 ):
        bestdiff = jolts[i] - jolts[i-1]
        diffs.append(bestdiff)

diff1, diff3 = diffs.count(1), diffs.count(3)
part1 = diff1 * diff3
print(part1)


# part 2

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
