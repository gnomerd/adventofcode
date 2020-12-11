#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex

seats = get_input(11).strip().splitlines()
seats = [ [seat for seat in seatrow]  for seatrow in seats ]

maxy = len(seats)
maxx = len(seats[0])

def getseat(x, y, seats):
    if( not x in range(0, maxx) or not y in range(0, maxy) ):
        return "."
    return seats[y][x]

def genMapString(seatmap, line="\n"):
    out = ""
    for seat in seatmap:
        for char in seat:
            out += char
        out += line

    return out

def printMap(seatmap):
    string = genMapString(seatmap)
    print(string)
    print("")


def getaround(x, y, curseats):
    out = dict()

    out[(x+1, y)] = getseat(x+1, y, curseats) # Right
    out[(x-1, y)] = getseat(x-1, y, curseats) # Left

    out[(x, y-1)] = getseat(x, y-1, curseats) # Up
    out[(x, y+1)] = getseat(x, y+1, curseats) # Down

    out[(x+1, y-1)] = getseat(x+1, y-1, curseats) # Right top
    out[(x+1, y+1)] = getseat(x+1, y+1, curseats) # Right bottom
    out[(x-1, y-1)] = getseat(x-1, y-1, curseats) # Left top
    out[(x-1, y+1)] = getseat(x-1, y+1, curseats) # Left bottom

    return out

def copySeatmap(curseats):
    return [ [seat for seat in seatrow]  for seatrow in curseats ]

def countThing(prop, taken, free, pr=False):
    staken, sfree = 0, 0
    for i in range(len(prop)):
        s = prop[i]
        if(s == "#" or s == "L"):
            if(s == "#"):
                staken = 1
            if( s == "L" ):
                sfree = 1
            #print(prop, i)
            break

    return taken+staken, free+sfree

def listToString(s):

    str1 = ""

    for ele in s:
        str1 += ele

    return str1

def getseen(x, y, seats):
    curseats = copySeatmap(seats)
    seen = dict()

    seenx = curseats[y]
    seenx[x] = "2"

    seenx = listToString(seenx)

    seenx = seenx.replace(".", "")
    seenx_left = seenx.split("2")[0][::-1]
    seenx_right = seenx.split("2")[1]



    seeny = []
    for iy in range(0, maxy): # NOTE: REVERSED ORDER    max = DOWN, min = UP
        s = getseat(x, iy, seats)
        if( iy == y ):
            s = "2"
        if( s != "." ):
            seeny.append( s )

    seeny = listToString(seeny)
    seeny_up = seeny.split("2")[0][::-1]
    seeny_down = seeny.split("2")[1]

    diagRU = [ getseat( x+i, y-i, curseats ) for i in range(0, maxx) if getseat( x+i, y-i, curseats ) != "." and i > 0 ] # Right up
    diagRD = [ getseat( x+i, y+i, curseats ) for i in range(0, maxx) if getseat( x+i, y+i, curseats ) != "." and i > 0 ] # Right down

    diagLU = [ getseat( x-i, y-i, curseats ) for i in range(0, maxx) if getseat( x-i, y-i, curseats ) != "." and i > 0 ] # Left up
    diagLD = [ getseat( x-i, y+i, curseats ) for i in range(0, maxx) if getseat( x-i, y+i, curseats ) != "." and i > 0 ] # Left down


    # if(x == 9 and y == 1):
    #     print("||", seenx)
    #     print("######||", "l:", seenx_left, "|", "r:", seenx_right)

    #     print("||", seeny)
    #     print("######||", "u:", seeny_up, "|", "d:", seeny_down)

    # print(seenx, "x")
    # print(seeny, "y")

    # print(diagRU, "RU")
    # print(diagRD, "RD")
    # print(diagLU, "LU")
    # print(diagLD, "LD")

    taken, free = 0, 0

    taken, free = countThing( seenx_right, taken, free )
    taken, free = countThing( seenx_left, taken, free )

    taken, free = countThing( seeny_up, taken, free )
    taken, free = countThing( seeny_down, taken, free )

    taken, free = countThing( diagRU, taken, free )
    taken, free = countThing( diagRD, taken, free )
    taken, free = countThing( diagLU, taken, free )
    taken, free = countThing( diagLD, taken, free )

    return taken, free

#print( "#", getseen(1, 0, seats) )


def calculateSeatmap2(curseats, i=0):
    newseats = copySeatmap(curseats)
    for y in range(0, maxy):
        for x in range(0, maxx):
            seat = getseat(x, y, curseats)
            if(seat == "."):
                continue
            taken, free = getseen(x, y, curseats)
            #print(taken, free, (x, y))

            if(taken == 0 and seat == "L"):
                newseats[y][x] = "#"
            elif( taken >= 5 and seat == "#" ):
                newseats[y][x] = "L"

    return newseats


seen = []
def calculateSeatmap(curseats, i=0):
    newseats = copySeatmap(curseats)
    for y in range(0, maxy):
        for x in range(0, maxx):
            seat = getseat(x, y, curseats)
            if(seat == "."):
                continue
            around = getaround(x, y, curseats)

            taken, free = 0, 0

            for coord, s in around.items():
                if( s == "#" ):
                    taken += 1
                elif( s == "L" ):
                    free += 1

            if(taken == 0 and seat == "L"):
                newseats[y][x] = "#"
            elif( taken >= 4 and seat == "#" ):
                newseats[y][x] = "L"

    return newseats




def countSeats(seatmap):
    mapstr = genMapString(seatmap, "")
    count  = mapstr.count("#")
    return count

def convertSeatmap(seatmap):
    out = []
    for seat in seatmap:
        seatstr = ""
        for char in seat:
            seatstr += char
        out.append(seatstr)

    return out

def checkEqual(seats1, seats2):

    return seats1 == seats2


def numSeats():
    lastSeatmap = copySeatmap(seats)
    i = 0
    while True:
        nextSeatmap = calculateSeatmap(lastSeatmap)

        check = checkEqual(nextSeatmap, lastSeatmap)

        if( check ):
            printMap(lastSeatmap)
            taken = countSeats(lastSeatmap)

            print("FOUND taken:", taken)
            break

        lastSeatmap = copySeatmap(nextSeatmap)


def numSeats2():
    lastSeatmap = copySeatmap(seats)
    i = 0
    while True:
        nextSeatmap = calculateSeatmap2(lastSeatmap)

        check = checkEqual(nextSeatmap, lastSeatmap)

        if( check ):
            printMap(lastSeatmap)
            taken = countSeats(lastSeatmap)

            print("2: FOUND taken:", taken)
            break

        lastSeatmap = copySeatmap(nextSeatmap)

numSeats2()

# printMap(seats)

# nextSeatmap = calculateSeatmap2(seats)
# printMap(nextSeatmap)

# nextSeatmap = calculateSeatmap2(nextSeatmap)
# printMap(nextSeatmap)
