#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex

navigation = get_input(12).splitlines()

def parseNav(nav):
    regex = r"^([A-Z]{1})([0-9]+)$"
    return re.match(regex, nav).groups()



boatfacing = "E" # start facing east
boatfacingClock = ["E", "S", "W", "N"]
boatfacingIndex = 0

boatpos = {
    "N": 0,
    "E": 0
}

boatpos2 = {
    "N": 0,
    "E": 0
}
waypoint = {
    "N": 1,
    "E": 10,
    "S": 0,
    "W": 0
}
pointkeys = "N E S W".split(" ")

# W = - E
# S = - N

def copyList(lst):
    return [elem  for elem in lst]

def move(dist, di):
    pos[di] += dist

def rotate( deg, boatclock, face ):
    clock = copyList(boatclock)
    clocklen = len(clock)

    facei = clock.index(face)
    rots = int(deg / 90)

    facei += rots

    while(facei < 0):
        facei += clocklen


    facei = facei % clocklen
    face = clock[facei]
    return face


from collections import OrderedDict
from itertools import islice, cycle


def shift_dict(dct, shift):
    shift %= len(dct)
    return OrderedDict(
        (k, v)
        for k, v in zip(dct.keys(), islice(cycle(dct.values()), shift, None))
    )



def calcDistance(pos):
    dist = 0
    for direction, units in pos.items():
        dist += abs(units)

    return dist

def runNav(nav, pos, facing, facingClock, facingIndex):
    na, num = parseNav(nav)
    num = int(num)

    if( na == "N" ):
        pos["N"] += num
    elif( na == "S" ):
        pos["N"] -= num

    elif( na == "E" ):
        pos["E"] += num
    elif( na == "W" ):
        pos["E"] -= num

    elif( na == "R" ):
        facing = rotate(num, facingClock, facing)
    elif( na == "L" ):
        facing = rotate(-num, facingClock, facing)

    elif( na == "F" ):
        if( facing == "N" or facing == "E" ):
            pos[facing] += num
        elif( facing == "W" ):
            pos["E"] -= num
        elif( facing == "S" ):
            pos["N"] -= num

    return pos, facing, facingIndex

def wayrotate( deg, point ):
    rots = (int(deg / 90)) * (-1)

    point = shift_dict(point, rots)

    return point

def forward( way, pos, num ):
    nor = (way["N"] - way["S"]) * num
    eas = (way["E"] - way["W"]) * num

    pos["N"] += nor
    pos["E"] += eas

    return pos

def runNavWay( nav, way, pos ):
    na, num = parseNav(nav)
    num = int(num)

    if( na in pointkeys ):
        way[na] += num
    elif( na == "R" ):
        way = wayrotate(num, way)
    elif( na == "L" ):
        way = wayrotate(-num, way)

    elif( na == "F" ):
        pos = forward( way, pos, num )

    return pos, way



for nav in navigation:
    boatpos, boatfacing, boatfacingIndex = runNav(nav, boatpos, boatfacing, boatfacingClock, boatfacingIndex)
    boatpos2, waypoint = runNavWay(nav, waypoint, boatpos2)

print("Part1:", calcDistance(boatpos))
print("Part2:", calcDistance(boatpos2))
