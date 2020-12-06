#!/usr/bin/env python

from aoc import get_input

nums = get_input(1).splitlines() 


def getNums(nums):
    numsLen = len(nums)

    for i in range(numsLen):
        for j in range(numsLen):
            if( nums[i] + nums[j] == 2020 ):
                return nums[i], nums[j]

    print("None found :(")
    return


def getNumsPart2(nums):
    numsLen = len(nums)
    for i in range(numsLen):
        for j in range(numsLen):
            for k in range(numsLen):
                if( nums[i] + nums[j] + nums[k] == 2020 ):
                    return nums[i], nums[j], nums[k]

    print("None found")

nums = list(map(int, nums))
print(nums)


# PART 1
x, y = getNums(nums)
theNum = x * y
print( f"1; OUTPUT: {getNums(nums)} | theNum: {theNum}" )


# PART 2
x, y, z = getNumsPart2(nums)
theNum = x * y * z
print(theNum)
