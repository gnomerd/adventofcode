#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex

data = get_input(16).strip()

stuff = data.split("\n\n")

params = stuff[0].split("\n")
myticket = stuff[1].split("\n")[1]
tickets = stuff[2].split("\n")
tickets.pop(0)


def parseParam(param):
    name, rnga1, rnga2, rngb1, rngb2 = re.match(r"([a-z\ ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", param).groups()

    rng1 = range(int(rnga1), int(rnga2) + 1)
    rng2 = range(int(rngb1), int(rngb2) + 1)

    return name, rng1, rng2

ranges = dict()
for i in range(len(params)):
    par = params[i]
    name, rng1, rng2 = parseParam(par)
    ranges[name] = (rng1, rng2)


def parseTicket(ticket):
    return [int(n) for n in ticket.split(",")]

badvals = []

goodtickets = [ti  for ti in tickets]
badtickets = []

for i in range(len(tickets)):
    if( i > 0 ):
        ticket = tickets[i]
        vals = parseTicket(ticket)

        for v in vals:
            checks = []
            for cl, rng in ranges.items():
                for r in rng:
                    checks.append( v in r )

            valid = any(check  for check in checks)

            if(not valid):
                badvals.append(v)
                break

        if( not valid ):
            print(f"Bad: {ticket=} {any(checks)=}")
            goodtickets.remove(ticket)
            badtickets.append(ticket)


print("\nPart1:", sum(badvals))

# freeranges = ranges

# def getClass(num):
#     out = None
#     for cl, rng in freeranges.items():
#         check1 = num in rng[0]
#         check2 = num in rng[1]
#         check = check1 or check2

#         if(check):
#             freeranges.pop(cl, None)
#             out = cl

#             break
#         else:
#             continue

#     return out

# def getClass2(num):
#     out = None
#     for cl, rng in ranges.items():
#         check1 = num in rng[0]
#         check2 = num in rng[1]
#         check = check1 or check2

#         if(check):
#             out = cl

#             break
#         else:
#             continue

#     return out

# print( getClass(3) )
# print( getClass(9) )
# print( getClass(18) )
# print("\n\n\n")

import itertools
import operator

def most_common(L):
    SL = sorted((x, i) for i, x in enumerate(L))
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        return count, -min_index
    return max(groups, key=_auxfun)[0]

seenindex = []
classIndex = dict()

#goodtickets.insert( 0, myticket )
print("####", len(goodtickets), "/" , len(tickets), "valid")

goodtickets = [ parseTicket(t)  for t in goodtickets ]


def possibleParams(num):
    possible = []
    for cl, rng in ranges.items():
        check1 = num in rng[0]
        check2 = num in rng[1]
        check = check1 or check2

        if(check):
            print(f"POSSIBLE {num=} {cl=}")
            possible.append(cl)

    return possible

from collections import defaultdict as dd

probIndex = dd(dict)

#print("22222", goodtickets[0])


# go through each param
# get possible indexs
# take least from possible
# add index to seen

print(params)

# for param, rng in ranges.items():
#     print("\nchecking param", param)
#     possible = {
#         0: 0,
#         1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0,
#         7: 0,
#         8: 0,
#         9: 0,
#         10: 0,
#         11: 0,
#         12: 0,
#         13: 0,
#         14: 0,
#         15: 0,
#         16: 0,
#         17: 0,
#         18: 0,
#         19: 0
#     }

#     for ticket in tickets:
#         for i in range(len(parseTicket(ticket))):
#             n = parseTicket(ticket)[i]

#             checks = []
#             for r in rng:
#                 checks.append( n in r )

#             valid = any(check  for check in checks)

#             print(f"Possible {rng=} {n=} {i=} {param=}", end="")

#             if(valid):
#                 print(" +1")
#                 possible[i] += 1
#             else:
#                 print("")

#     probIndex[param] = possible

def numIsValid(num, rng):
    checks = []
    for r in rng:
        checks.append( num in r )

    valid = any(check  for check in checks)
    return valid


for i in range( len(goodtickets[0]) ):
    validcls = []

    for ticket in goodtickets:
        num = ticket[i]

        for cl, rng in ranges.items():
            valid = numIsValid(num, rng)

            if(valid):
                validcls.append(cl)

    probIndex[i] = validcls

    
seenIndex = []
seenValid = []
paramPos = dict()
print("\n\nTHING")

for chari in range( len(goodtickets[0]) ):
    if( not chari in seenIndex ):
        valids = probIndex[chari]

        least = 99999999
        leastparam = None
        for v in valids:
            if( valids.count(v) < least and not v in seenValid ):
                least = valids.count(v)
                leastparam = v

        print(f"{least=} {leastparam=} {valids=}")

        paramPos[chari] = leastparam

        seenIndex.append(chari)
        seenValid.append(leastparam)

print(paramPos)


# for param, pos in probIndex.items():
#     if(param in seen):
#         continue

#     print("\n", param)

#     for i, val in probIndex[param].items():
#         print(i, val)


print(paramPos)

# for i in range(len(goodtickets[0])):
#     posParams = [ possibleParams( goodtickets[0][i] ) ]

#     for j in range(1, len(goodtickets)):
#         tick = goodtickets[j]
#         n = tick[i]
#         pos = possibleParams( n )

#         posParams.append(pos)

#     probIndex[i] = posParams


# print(len(probIndex[19]))

# def checkParamForIndex(i, p):
#     params = probIndex[i]
#     # check = all( p in ticket  for ticket in params )
#     # print("###############", check, len(params))




# for i in range(len(goodtickets[0])):
#     num = goodtickets[0][i]
#     numcl = [ getClass(num) ]

#     for j in range(0, len(goodtickets)):
#         tick = goodtickets[j]
#         n = tick[i]
#         nclass = getClass2(n)
#         if(nclass):
#             numcl.append(nclass)

#     common = most_common(numcl)
#     same_count = numcl.count(common)
#     r = (same_count / len(goodtickets)) * 100
#     print(f"{i=} {num=} {common=} {same_count=} {r=}% {numcl[0]=}")
#     probIndex[common][i] = r

# print(probIndex)

# paramIndex = dict()

# for parameter, probs in probIndex.items():
#     lastProb = 0
#     bestIndex = None
#     for i, prob in probs.items():
#         if( prob > lastProb ):
#             lastProb = prob
#             bestIndex = i

#     paramIndex[parameter] = bestIndex

# print("######", paramIndex)


# for ticket in tickets:
#     if( ticket in badtickets ):
#         continue
#     #print(ticket)

#     p = parseTicket(ticket)

#     for i in range(len(p)):
#         check = not i in seenindex

#         if( check ):

#             num = p[i]
#             cl = getClass(num)
#             classIndex[cl] = i
#             seenindex.append(i)

#             continue


myticket = parseTicket(myticket)
thenums = []

# for cl, i in paramIndex.items():
#     if( "departure" in cl ):
#         thenums.append( myticket[i] )

print(thenums)

import math

print("  1409959524847 !=")
print("#",math.prod(thenums))
print("  21095351239483")
print("  30145908219919 reverse")

print(sum(thenums))

print(classIndex)
