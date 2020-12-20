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


mapWidth = len(pics) ** (1/2)

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


def getFits(borders, fits=fitsDict, ignore=[]):
    #print(fits)
    #print("\n#", borders, "\n")
    ignoreLen = len(ignore)
    borLen = len(borders)

    print(ignoreLen, borLen)

    if(ignoreLen >= borLen):
        print("goodbye")
        return fits # if there is nothing to do then return the result

    newborders = copy(borders)
    for pid, border in borders.items(): # borders[pid]
        #print(f"\nChecking {pid=}")
        if( pid in ignore ):
            continue

        for pos, bor in border.items(): # check each border : borders[pid][pos]

            print(f"##Border {pid=} {pos=} {bor=}")

            for pid2, border2 in borders.items(): # check for others borders ;  borders[pid2]
                if(pid2 == pid or pid2 in ignore):
                    continue

                for pos2, bor2 in border2.items(): # check for other matching border ; borders[pid2][pos2]

                    check, newBor2 = borderCheck(bor, bor2)
                    print(f"####Border2 {pid2=} {pos2=} {bor2=} {newBor2=} {check=}")

                    if(check): # if the two borders match:
                        fits[pid] = dict()
                        fits[pid][pos] = (pid2, pos2)

                        ignore.append(pid)

        fits[pid] = fits[pid] or {"E": None} # It has to end somewhere

    return getFits(newborders, fits, ignore) # do the other borders

print(picBorders)

fits = getFits(picBorders, fitsDict)
print("------------")
print(fits)

picmap = dd(dict) # inp: coord [][] -> pid
coords = dict() # inp: pid -> out: coord (tuple)

pidList = fits.keys()
firstID = None
for pid in pidList:
    firstID = pid
    break

#      y  x
picmap[0][0] = firstID
print(firstID)

for pid, fit in fits.items():
    if(pid == firstID):
        continue

    for pos, fitin in fit.items():
        if(pos != "E"):
            fitID, fitDIR = fitin[0], fitin[1]

            print(f"{pid=} {pos=} : {fitID=} {fitDIR=}")
        else:
            continue
