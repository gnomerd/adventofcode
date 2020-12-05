#!/usr/bin/env python

from aoc import get_input
import re

seats = get_input(5).splitlines()
curSeats = seats

test = "BBFFBBFRLL"

maxRow = 128
maxCol = 8

seatMap = [ [seat for  seat in range(0, maxCol)]  for seat in range(0, maxRow) ]

def toList(string):
    list = []
    list[:0] = string
    return list

def splitList(l):
    half = int(len(l) / 2)
    return l[:half], l[half:]

def parseRows(x, row):
    no = None
    for coord in x:
        if(coord == "L"):
            row, no = splitList(row)
        elif(coord == "R"):
            no, row = splitList(row)

    return row




def parseThing(x:str):

    regexThing = re.split(r"(R|L)", x)

    rowsList = regexThing[1:]
    rows = ""
    for char in rowsList:
        rows += char

    rows = toList(rows)

    cols = regexThing[0]
    seat = toList(cols)

    seats = seatMap
    no = None

    curCol = [col  for col in range(0, 128)]

    for coord in seat:
        if( coord == "F" ):
            seats, no = splitList(seats)

            spl = splitList(curCol)
            curCol = spl[0]

        elif( coord == "B" ):
            no, seats = splitList(seats)

            spl = splitList(curCol)
            curCol = spl[1]

        else:
            break

    chair = parseRows(rows, seats[0])[0]

    return curCol[0], chair


def getSeatID(coords):
    return coords[0] * 8 + coords[1]



# Part 1

high = ((0,0), 0)

usedSeats = seatMap

for seat in seats:
    coord = parseThing(seat)

    seatid = getSeatID(coord)

    usedSeats[coord[0]][coord[1]] = False

    if(seatid > high[1]):
        high = (coord, seatid)


# Part 2

mySeat = None

for s in range(len(usedSeats)):
        for r in range(0, 8):
            if(usedSeats[s][r]):
                if( s in range(1, 126) ):
                    #print("(FIRST) None at", s, r)
                    mySeat = mySeat or (s, r)
                    break

        if(mySeat):
            break


print("Part1:", high[1])
print("Part2:", getSeatID(mySeat))
