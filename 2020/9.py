#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex

nums = list(map(int, get_input(9).splitlines()))

def checkValid(nums, numsum):
    for num1 in nums:
        for num2 in nums:
            if( num1 + num2 == numsum and num1 != num2 ):
                return [num1, num2], numsum

    return False, numsum

def checkIfNumValid( amble, index ):
    prevNums = nums[index-amble:index]
    numsum = nums[index]
    sumnumbers, numsum2 = checkValid(prevNums, numsum)

    return sumnumbers, numsum2


amble, invalid, invalidindex = 25, None, None

for i in range(len(nums)):
    if(i > amble-1):
        valid = checkIfNumValid(amble, i)
        if( not valid[0] ):
            invalid, invalidindex = valid[1], i
            break

stop, foundnums = False, []
for i in range(len(nums)):
    for rangei in range(len(nums)):
        numlist = nums[i-rangei:i]
        if( not invalid in numlist ):
            sumnums = sum(numlist)

            if(sumnums == invalid):
                foundnums = numlist
                stop = True
                break
    if(stop):
        break

minnum, maxnum = min(foundnums), max(foundnums)

print("Part1:", invalid)
print("Part2:", minnum + maxnum)
