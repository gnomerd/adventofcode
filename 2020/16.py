#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex
from collections import defaultdict as dd

data = get_input(16).strip()

stuff = data.split("\n\n")

params = stuff[0].split("\n")
myticket = stuff[1].split("\n")[1]
tickets = stuff[2].split("\n")
tickets.pop(0)


def parseParam(param):
    name, rnga1, rnga2, rngb1, rngb2 = re.match(r"(\w+ *\w*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", param).groups()

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

myticket = parseTicket(myticket)

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
            goodtickets.remove(ticket)


tickets = [parseTicket(t) for t in goodtickets]

ticketlen = len(tickets[0])



works = dd(set)

for i in range(ticketlen):
    clthing = dict()
    for cl, rng in ranges.items():
        clthing[cl] = 0

    for ticket in goodtickets:
        ticket = parseTicket(ticket)
        num = ticket[i]

        for cl, rng in ranges.items():
            clcount = 0
            if(num in rng[0] or num in rng[1]):
                clcount += 1
                clthing[cl] += clcount


    for cl, count in clthing.items():
        if( count == len(goodtickets) ):
            works[i].add(cl)


used = set()
while( any( [len(paramwork) > 1 for paramwork in works.values()] ) ):
    for index, cl in works.items():
        if(len(cl) > 1):
            works[index] = (cl | used) ^ used
        else:
            used.add(next(iter(cl)))

thenums = []
for i, cl in works.items():
    num = myticket[i]
    cl = list(cl)

    if( "departure" in cl[0] ):
        thenums.append(num)



import math

print("Part 1", sum(badvals))
print("Part 2:", math.prod(thenums))
