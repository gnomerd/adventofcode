#!/usr/bin/env python

from collections import defaultdict as dd
from aoc import get_input # AoC
import re # regex
import numpy as np
from copy import deepcopy as copy

from sys import setrecursionlimit
setrecursionlimit(20000)

data = get_input(20).strip()

pics = dict()
for genpic in data.split("\n\n"):
    foundTitle = None

    for i, row in enumerate(genpic.splitlines()):
        if(foundTitle == None):
            titleCheck = re.match(r"^Tile ([0-9]+):", row)

            if(titleCheck != None):
                foundTitle = titleCheck[1]
                pics[foundTitle] = []

        else:
            try:
                pics[foundTitle].append( list(row) )
            except:
                pics[foundTitle] = []
                pics[foundTitle].append( list(row) )


for pid, pic in pics.items():
    pics[pid] = np.asarray(pic)


mapWidth = int(len(pics) ** (1/2))

def compileBorder(row):
    out = ""
    for char in row:
        out += char

    return out

def compileSideBorder(pic, xOffset=0):
    out = ""
    for row in pic:
        out += row[xOffset]

    return out


# check 4 border locations, up, down, left, right
picBorders = dict()
def genBorders(picid):
    pic = pics[picid]

    ## compile its borders
    borders = dict()
    borders["U"] = compileBorder(pic[0])
    borders["R"] = compileSideBorder(pic, -1)
    borders["D"] = compileBorder(pic[-1]) # up: 0, right: 1, down: 2, left: 3
    borders["L"] = compileSideBorder(pic, 0)

    return borders

for pid, pic in pics.items():
    picBorders[pid] = genBorders(pid)


# picmap = dict() # map of the arranged pics

def flip(otherside):
    # 0 up, 1 right, 2 down, 3 left

    sidething = { # used to rotate as the rotation is allways the opposite relative to the whole system
        "U": "D",
        "R": "L",
        "D": "U",
        "L": "R"
    }

    newotherside = sidething[otherside]

    # update the connected tiles rotation

    return newotherside

def borderCheck(border, other):
    other_rev = other[::-1]

    if( border == other or border == other_rev ):
        return True, border
    else:
        return False, other

fitsDict = dd(dict)

# fits struc
#
# fits[id] = { "L": (otherid, rotation) }
# where key = "L", "R", "U", "D", "UL", "UR", "DL", "DR"
# otherid is the one that fits
# rotation is the other that fits rotation to be able to fit


def getFits(borders, fits=fitsDict, ignore=[], ignoreBorder=[]):
    #print(fits)
    #print("\n#", borders, "\n")
    ignoreLen = len(ignoreBorder)
    borLen = len(borders)

    if(ignoreLen >= borLen):
        #print("goodbye")
        return fits # if there is nothing to do then return the result

    newborders = copy(borders)
    for pid, border in borders.items(): # borders[pid]
        #print(f"\nChecking {pid=}")
        if( pid in ignore ):
            continue

        for pos, bor in border.items(): # check each border : borders[pid][pos]

            #print(f"##Border {pid=} {pos=} {bor=}")

            for pid2, border2 in borders.items(): # check for others borders ;  borders[pid2]
                if(pid2 == pid or pid2 in ignore or border2 in ignoreBorder):
                    continue

                for pos2, bor2 in border2.items(): # check for other matching border ; borders[pid2][pos2]

                    check, newBor2 = borderCheck(bor, bor2)
                    #print(f"####Border2 {pid2=} {pos2=} {bor2=} {newBor2=} {check=}")
                    if( not check ):
                        continue

                    if(check): # if the two borders match:
                        fits[pid] = fits[pid] or dict()
                        fits[pid][pos] = [pid2, pos2]

                        #ignore.append(pid)
                        ignoreBorder.append(bor2)

        fits[pid] = fits[pid] or {"E": None} # It has to end somewhere

    return getFits(newborders, fits, ignore) # do the other borders


fits = getFits(picBorders, fitsDict)


fitsListKeys = list(fits.keys())



#picmap = [["#" for x in range(mapWidth)] for y in range(mapWidth)] # inp: coord [][] -> pid
picmap = dd(dict)
piccoords = dict() # inp: pid -> out: coord (tuple)

seenPics = []

def translatePos(pos, x, y):
    if(pos == "U"):
        return x, y-1
    elif(pos == "D"):
        return x, y+1
    elif(pos == "L"):
        return x-1, y
    elif(pos == "R"):
        return x+1, y



def setPos(pid, x, y, pmap, coords, seen=[]):
    pmap[y] = pmap[y] or dict()
    pmap[y][x] = pid

    coords[pid] = (x, y)
    seen.add(pid)
    return seen

def getPos(x, y, pmap):
    try:
        pid = pmap[y][x]
        if( pid == "----" ):
            return None
        else:
            return pid
    except:
        return None

def printMap(pmap):
    for y in range(mapWidth):
        row = pmap[y]

        for x in range(mapWidth):
            try:
                print( row[x], end="  " )
            except:
                print("----", end="  ")

        print("\n")

def findContainer(sid, fits):
    foundContainers = []
    for pid, fit in fits.items():
        for f in fit.values():
            if(sid in f):
                foundContainers.append(pid)

    return foundContainers


corners = []
cornersPos = dict()

# thingid = "1129"
# thing = fits[thingid]["U"]
# fits[thingid]["D"] = thing
# fits[thingid].pop("U")


for pid, cont in fits.items():
    if(len(cont) == 2):
        corners.append(pid)
        print("corner:", pid, cont)


prod = 1
for c in corners:
    prod *= int(c)

print("Part1:", prod)

print("\n\n")


seenid = set()

# know the corners
# start from corner 1 then 2, then update 3 and 4
#
# 1---------2
# |         |
# |  stuff  |
# |  here   |
# |         |
# 3---------4

# append the first corner at 0, 0

mapW = mapWidth - 1

for y in range(mapWidth):
    for x in range(mapWidth):
        picmap[y][x] = "----"

seenid = setPos(corners[0], 0, 0, picmap, piccoords, seenid) # some corner
print("####", corners)

i = 0

def getRotIndex(rot):
    return ["U", "R", "D", "L"].index(rot)

def rotateDirs(pid, rot, fits):
    irot = getRotIndex(rot)
    cont = fits[pid]

    newcont = copy(cont)

    for pos, stuff in cont.items():
        ipos = getRotIndex(pos)
        diff = ipos - irot

        while(diff < 0):
            diff += 4

        newpos = ["U", "R", "D", "L"][(ipos + diff) % 4]
        newcont[newpos] = stuff

    fits[pid] = newcont
    return fits[pid]

# U -> L
# => new = U -> rotate(L)

def genPicMap(pmap=picmap, pcoords=piccoords, fits=fits, seenid=set()):
    for y in range(mapWidth):
        for x in range(mapWidth):
            pidAtPos = getPos(x, y, pmap)

            if(pidAtPos):
                fit = fits[pidAtPos] # possible connections
                print(f"\n{pidAtPos}: {fit}")

                for pos, child in fit.items():
                    childID, childRot = child[0], child[1]
                    if(childID in seenid):
                       continue

                    nx, ny = translatePos(pos, x, y)
                    pidInSpace = getPos(nx, ny, pmap) # check if there is something there
                    print(f"{pos=} {child=} : {pidInSpace=} {nx,ny=}")

                    if(pidInSpace or nx < 0 or ny < 0):
                        continue

                    # update the childs rotation
                    fits[childID] = rotateDirs(childID, pos, fits)

                    # add it to the pos
                    seenid = setPos(childID, nx, ny, pmap, pcoords, seenid)

while( True ):
    genPicMap()
    print("")
    printMap(picmap)
    breakpoint()
