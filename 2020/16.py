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


print("\nPart1:", sum(badvals))


tickets = [parseTicket(t) for t in goodtickets]

ticketlen = len(tickets[0])


# make seen list for param and index
#
# go through all indexes, i=0
# make list of possibleParams for that i
# # go through all tickets for i
# # # go through all params
# # # # check if ticket[i] is in param range
# # # # # if not then remove param from iparams
# # # # # else next param
# take first param
# exclude param from list and exclude index from list
# next index



seenparams = []
seenindex = []

paramsIndex = dict()

def getPosParams(i):
    iparams = dict()
    possibleParams = []
    for p in params:
        paramclass, rng1, rng2 = parseParam(p)
        iparams[paramclass] = (rng1, rng2)
        possibleParams.append(paramclass)

    for t in goodtickets:
        ticket = parseTicket(t)
        num = ticket[i]

        for param, rng in iparams.items():

            check = num in rng[0] or num in rng[1]
            if(not check and param in possibleParams):
                possibleParams.remove(param)
            else:
                continue

    return possibleParams


for i in range(ticketlen):
    posparam = getPosParams(i)
    posparam.sort(key=len)
    print(posparam)

    thisparam = None

    for cl in posparam:
        if(not cl in seenparams):
            thisparam = cl
            seenparams.append(cl)
            break

    paramsIndex[i] = thisparam

print("####", paramsIndex)
thenums = []

for i, cl in paramsIndex.items():
    print(f"{cl}: {parseTicket(myticket)[i]}")

    if(cl):
        if( "departure" in cl ):
            thenums.append(parseTicket(myticket)[i])




print(thenums)

import math

print("  1409959524847 !=")
print("#",math.prod(thenums))
print("  21095351239483")
print("  30145908219919 reverse")

print(sum(thenums))

