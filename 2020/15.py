#!/usr/bin/env python

from aoc import get_input # AoC
from collections import defaultdict as dd

nums = list(map( int, get_input(15).split(",")))

firstNums = dd(list)

for i, n in enumerate(nums):
    firstNums[n].append(i)

def numbers(maxt):
    num = nums[-1]
    for i in range(len(nums), maxt):
        numsSeen = len(firstNums[num])

        if( numsSeen > 1 ):
            num = firstNums[num][-1] - firstNums[num][-2]
        else:
            num = 0

        #print(f"{num=} {i=} {nums=}")
        firstNums[num].append(i)

    return num


#maxturn = 2020
#maxturn = 30000000

maxturn = 10
print(numbers(maxturn))
