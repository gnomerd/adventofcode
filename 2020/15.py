#!/usr/bin/env python

from aoc import get_input # AoC
from collections import defaultdict

nums = list(map( int, get_input(15).split(",")))

firstNums = defaultdict(list)

i = 0
for n in nums:
    firstNums[n].append(i)
    i += 1


def addSeen(num):
    firstNums.add(num)

def copyNums(lst):
    return [elem for elem in lst]

def getFirstNum(num, start=len(firstNums)):
    i = start
    while i >= 0:
        n = firstNums[i]
        if( n[0] == num ):
            return n[1]
        i -= 1


# def getNextNum(i):
#     if( i >= len(nums) ):
#         lastNum = nums[i-1]
#         newNums = nums[:i-1]

#         if( lastNum == nums[i-2] ):
#             nums.append(1)
#             addSeen(1)

#         elif( not lastNum in firstNums ): # new number
#             nums.append(0)
#             addSeen( (lastNum, i-1) )

#         elif( lastNum in firstNums ): # spoken before
#             ei= getFirstNum(lastNum)
#             fi = getFirstNum(lastNum, ei-1)
#             newN = ei - fi # diff is still the same if ei = ei+1
#             nums.append(newN)
#             addSeen( (newN, i-1) )


# turn = 3

# while True:
#     if( turn < 30000000 ):
#         getNextNum(turn)
#         print(turn, "/30000000")
#         turn += 1
#     else:
#         print(nums[-1])
#         break




def numbers(maxt):
    num = nums[-1]
    prevnum = None
    for i in range(len(nums), maxt):
        numsSeen = len(firstNums[num])

        if( numsSeen > 1 ):
            num = firstNums[num][-1] - firstNums[num][-2]
        else:
            num = 0

        print(f"{num=} {i=} {nums=}")
        firstNums[num].append(i)

    return num




turn = 3
#maxturn = 30000000
#maxturn = 2020
maxturn = 10
print("0, 3, 6, 0, 3, 3, 1, 0, 4, 0")
print(numbers(maxturn))
