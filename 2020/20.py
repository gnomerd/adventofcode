#!/usr/bin/env python

from collections import defaultdict as dd
from aoc import get_input # AoC
import re # regex
import numpy as np

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

print(pics["3079"])

fits = dict()

# fits struc
#
# fits[id] = { "L": (otherid, rotation) }
# where key = "L", "R", "U", "D", "UL", "UR", "DL", "DR"

def compileBorder(row):
    out = ""
    for char in row:
        out += char

    return out

def compileSideBorder(pic,  xOffset=0):
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
    borders[0] = compileBorder(pic[0])
    borders[1] = compileSideBorder(pic, -1)
    borders[2] = compileBorder(pic[-1]) # up: 0, right: 1, down: 2, left: 3
    borders[3] = compileSideBorder(pic, 0)

    return borders

for pid, pic in pics.items():
    picBorders[pid] = genBorders(pid)


# picmap = dict() # map of the arranged pics

def rotateTile(otherside):
    # 0 up, 1 right, 2 down, 3 left

    sidething = { # used to rotate as the rotation is allways the opposite relative to the whole system
        0: 2,
        1: 3,
        2: 0,
        3: 1
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

def getFits(picid, ignoreid):
    borders = picBorders[picid]

    seenborders = []
    attachedTiles = []

    # if some border match, i.e. this[2] match other[1] then rotate and/or flip other?
    # dont actually have to arrange the map, just get stuff that fits together and their IDs
    #
    # probably gonna be in part 2 idk

    match = False
    matchID = None
    selfSide = None
    matchSide = None
    matchFlipped = False

    prevTile = None

    for side, border in borders.items(): # TODO: make recursive instead and flip (np.fliplr) (and for up-down)
        # check other borders
        selfSide = side

        for pid, bor in picBorders.items():
            if(pid == picid or pid == ignoreid):
                continue

            # print("Checking", pid, f"{attachedTiles=}")


            for pos, line in bor.items(): # top and bottom matching
                if(not pos in [0, len(bor)-1]):
                    continue

                if(line in seenborders):
                    continue

                check, newborder = borderCheck(border, line)
                print("TB Checking border", pos, ":", line, f"{newborder=} {line=} : {border=}")


                if( check ):
                    matchID = pid
                    matchSide = pos
                    matchFlipped = line == newborder # flipped from matchSide axis

                    if( newborder != line ):
                        picBorders[pid][pos] = newborder # flip that border if flipped
                        otherside = rotateTile(pos)
                        picBorders[pid][otherside] = picBorders[pid][otherside][::-1] # flip the other side too

                    match = True
                    attachedTiles.append(matchID)
                    seenborders.append(line)
                    prevTile = matchID
                    print("MATCH")
                    break

            if(not match):

                border_left, border_right = "", ""
                for y, line in bor.items():
                    border_left += line[0]
                    border_right += line[-1]

                print(f"LR Checking border : {border_left=} {border_right=}")
                check_left, newborder_left = borderCheck(border_left, line)
                check_right, newborder_right = borderCheck(border_right, line)

                if(check_left):
                    pos = 3
                    matchID = pid
                    matchSide = pos
                    matchFlipped = border_left == newborder_left # flipped from matchSide axis

                    if( newborder_left != line ):
                        picBorders[pid][pos] = newborder_left # flip that border if flipped
                        otherside = rotateTile(pos)
                        picBorders[pid][otherside] = picBorders[pid][otherside][::-1] # flip the other side too

                    match = True
                    attachedTiles.append(matchID)
                    seenborders.append(line)
                    prevTile = matchID
                    print("MATCH")
                    break
                elif(check_right):
                    pos = 1
                    matchID = pid
                    matchSide = pos
                    matchFlipped = border_right == newborder_right # flipped from matchSide axis

                    if( newborder_right != line ):
                        picBorders[pid][pos] = newborder_right # flip that border if flipped
                        otherside = rotateTile(pos)
                        picBorders[pid][otherside] = picBorders[pid][otherside][::-1] # flip the other side too

                    match = True
                    attachedTiles.append(matchID)
                    seenborders.append(line)
                    prevTile = matchID
                    print("MATCH")
                    break



            else:
                break

    if(match):
        return [selfSide, matchID, matchSide, matchFlipped]


mapWidth = int(len(pics) ** (1/2))

tilemap = np.empty([mapWidth, mapWidth], dtype=str)
print("")
print(tilemap)

aligns = dict()

#for pid, pic in pics.items():
nextTile = None
prevTile = None

for key in pics.keys():
    nextTile = key
    prevTile = key
    break


seenTiles = []
loop = False
while(not loop):
    fits = getFits(nextTile, prevTile)
    aligns[nextTile] = fits

    print(fits)

    # prevTile = nextTile
    # nextTile = fits[1]

    # if(nextTile in seenTiles):
    #     loop = True
    #     break

    # seenTiles.append(prevTile)
    # print(prevTile, nextTile, seenTiles)

print(aligns)

def copyList(ls):
    return [elem for elem in ls]

# ################
# exit()
# ################






def rotateNumTo(numrot, tonum):
    tonum = rotateTile(tonum)
    # numrot -> tonum

    # get num of rotations clockwise
    rots = numrot - tonum
    newrot = numrot + rots

    while(newrot < 0):
        newrot += 4

    newrot = newrot % 4

    return newrot


# ----------------------------------------------
# |    0         1         2            3      |
# |[selfSide, matchID, matchSide, matchFlipped]|
# ----------------------------------------------

# for pid, fit in aligns.items():
#     fitid = fit[1]

#     conRot = fit[0]
#     myRot = fit[2]

#     newrot = rotateNumTo(myRot, conRot)
#     #print(f"{pid=} {fitid=} : {conRot=} {myRot=} : {newrot=}")

#     aligns[fitid][0] = newrot # make others relative

print("\n\n----")
rotmap = dd(dict) # inp: coords
rotcoords = dd(tuple) # inp: pid

seenpid = []

i = 0
for pid, align in aligns.items():
    print(pid, align)

    if( i == 0 ):
        coords = (0, 0)
        rotmap[coords[1]][coords[0]] = pid
        rotcoords[pid] = coords
        seenpid.append(pid)
        continue



    selfside = align[0]
    matchside = align[2]

    matchid = align[1]



# while(len(rots) < len(pics)):

#     for pid, fit in aligns.items():
#         if(len(seenpid) >= len(aligns)):
#             break

#         if(pid in seenpid):
#             continue

#         seenpid.append(pid)

#         if(len(rotmap) <= 0):
#             rotmap[0][0] = pid
#             rots[pid] = (0, 0)

#         fitid = fit[1]

#         conRot = fit[0]
#         myRot = fit[2]

#         coords = rots[pid]
#         print(f"{pid} : {coords} : {fitid} |", end=" ")

#         if(len(coords) < 2):
#             print("no coords")
#             continue

#         x, y = coords[0], coords[1]

#         if(conRot == 0):
#             # put the connected one above it
#             # x y is reversed because lists index and stuff
#             rots[fitid] = (x, y-1)
#             print(f"new coord: {rots[fitid]}")

#         elif(conRot == 1):
#             # right of
#             rots[fitid] = (x+1, y)
#             print(f"new coord: {rots[fitid]}")

#         elif(conRot == 2):
#             # down of
#             rots[fitid] = (x, y+1)
#             print(f"new coord: {rots[fitid]}")

#         elif(conRot == 3):
#             # left of
#             rots[fitid] = (x-1, y)
#             print(f"{fitid} new coord: {rots[fitid]}")


# print(rots)

# def rotateClock( rots, picRot, face ):
#     clock = copyList(picRot)
#     clocklen = len(clock)

#     facei = face

#     facei += rots

#     while(facei < 0):
#         facei += clocklen


#     facei = facei % clocklen
#     face = clock[facei]
#     return face




# fitmap = dict()
# for pid, fits in aligns.items():
#     side, fitid, fitside, flipside = fits

#     newside = rotateTile(side, fitside)
