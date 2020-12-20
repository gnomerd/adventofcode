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

fitsDict = dd(set)

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

    print(ignoreLen, borLen)

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
                        fits[pid][pos] = (pid2, pos2)

                        #ignore.append(pid)
                        ignoreBorder.append(bor2)

        fits[pid] = fits[pid] or {"E": None} # It has to end somewhere

    return getFits(newborders, fits, ignore) # do the other borders

print(picBorders)

fits = getFits(picBorders, fitsDict)
print("------------")
print(fits)


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
    seen.append(pid)
    return seen

def printMap(pmap):
    print(" #---# ")
    for y in range(mapWidth, -5, -1):
        row = pmap[y]

        for x in range(-8, mapWidth):
            try:
                print( row[x], end=" " )
            except:
                print("----", end=" ")

        print("")
    print(" #---# ")


def genTheMap(pmap, coords, seenPID=[], fits=fits):
    i = 0

    for pid, fit in fits.items():
        print("#", pid, fit)
        if( i == 0 ):
            seenPID = setPos(pid, 0, 0, pmap, coords, seenPID)
            print(f"{pid} at 0, 0")

            for cpos, child in fit.items():
                cx, cy = translatePos(cpos, 0, 0)
                print(f"{child[0]} at {cx} {cy}")
                seenPID = setPos(child[0], cx, cy, pmap, coords, seenPID)

            i += 1
        else:
            if( pid in seenPID ): # check if pid is in map
                # if exists then check around it
                print(f"{pid=} : {fit=}")

                for cpos, child in fit.items():
                    if(not child[0] in seenPID):

                        x, y = coords[pid]
                        cx, cy = translatePos(cpos, x, y)

                        print(f"{child=}: {child[0]} at {cx} {cy}")

                        seenPID = setPos(child[0], cx, cy, pmap, coords, seenPID)

            else:
                print(f"{pid=} : {fit=}")

                for seenp in seenPID: # check if anyone has the PID as a connection
                    if(seenp == pid): # this should not happen
                        continue

                    fit2 = fits[seenp]

                    for pos, fit in fit2.items():
                        fid = fit[0]
                        if( fid == pid ): # found it
                            pos = flip(pos) # flip it because it is reversed

                            x, y = coords[seenp] # get the seen ones pos
                            cx, cy = translatePos(pos, x, y) # get our pos

                            seenPID = setPos(pid, cx, cy, pmap, coords, seenPID)


        # NOTE: LOOP AGAIN IF LOST PIDS
            i += 1

    if(len(pmap) < len(pics)):
        return genTheMap(pmap, coords, seenPID, fits)
    else:
        return fits

genTheMap(picmap, piccoords)

printMap(picmap)
