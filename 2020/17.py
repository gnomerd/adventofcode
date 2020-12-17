#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex
import numpy as np
from copy import deepcopy as copy

config = get_input(17).strip().split("\n")

for i in range(len(config)):
    newlst = []
    newlst[:0] = config[i]
    config[i] = newlst




# network is a simple 3D cube

# x * x * x

initlen = len(config[0])

print(np.asarray(config))
print(f"{initlen=}")

cube = np.asarray([ np.zeros((initlen,initlen), int)  for z in range(initlen) ])

cube4 = np.asarray([[ np.zeros((initlen,initlen), int)  for z in range(initlen) ] for w in range(initlen) ])

#apply config to network

cubelen = initlen
cubelen4 = initlen

configZ = 1
#cube[configZ] = config

for iy in range(len(config)):
    for ix in range(len(config)):
        if(config[iy][ix] == "."):
            cube[configZ][iy][ix] = 0
        else:
            cube[configZ][iy][ix] = 1

for iy, row in enumerate(config):
    for ix, node in enumerate(row):
        val = 0
        if( node == "#" ):
            val = 1

        cube4[1][1][iy][ix] = val

print(cube4, cube4.shape)


def getpos(x, y, z, net=cube):
    netlen = net.shape[0]
    if(x in range(netlen) and y in range(netlen) and z in range(netlen)):
        return net[z][y][x]
    else:
        return None

def setpos(x, y, z, val, net=cube):
    netlen = net.shape[0]
    if( x in range(netlen) and y in range(netlen) and z in range(netlen) ):
        net[z][y][x] = val
    else:
        return None

def countaround(x, y, z, net=cube):
    px = [-1, 0, 1]
    py = [-1, 0, 1]
    pz = [-1, 0, 1]

    around = dict()
    count = 0
    checkcount = 0

    for iz in pz:
        for iy in py:
            for ix in px:
                pos = (x+ix, y+iy, z+iz)

                if( pos != (x, y, z) ):
                    checkcount += 1

                    val = getpos(pos[0], pos[1], pos[2], net)
                    around[pos] = val

                    if( val ):
                        count += val

    return count, checkcount




offset4 = set()
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            for w in range(-1, 2):
                if( (x, y, z, w) != (0, 0, 0, 0) ):
                    offset4.add( (x, y, z, w) )

def getpos4(x, y, z, w, net=cube4):
    netlen = net.shape[0]
    if(x in range(netlen) and y in range(netlen) and z in range(netlen) and w in range(netlen)):
        return net[w][z][y][x]
    else:
        return None

def setpos4(x, y, z, w, val, net=cube4):
    netlen = net.shape[0]
    if(x in range(netlen) and y in range(netlen) and z in range(netlen) and w in range(netlen)):
        net[w][z][y][x] = val

def countaround4D(x, y, z, w, net=cube4):
    count = 0
    checkcount = 0
    for diff in offset4:
        val = getpos4(x+diff[0], y+diff[1], z+diff[2], w+diff[3], net)
        checkcount += 1
        if( val == 1 ):
            count += 1
    return count, checkcount


def printLayer(z, net=cube):
    print("Layer ", z)
    for l in net[z]:
        for char in l:
            #print(f"{char} ", end="")
            if(char):
                print("# ", end="")
            else:
                print(". ", end="")
        print("")
    print("----")


def expandCube(net=cube, expand=1):
    net = np.pad(net, pad_width=expand, mode='constant', constant_values=0)
    cubelen = net.shape[0]
    return net, cubelen



#expandCube(cube, cycles)
cycles = 6
def runCycle(net, c=0, maxc=cycles, expand=False, ignoreCfgLayer=False):
    if( not c < maxc ):
        print("Done")
        return net

    if(expand):
        net, cubelen = expandCube(net, 1)
    newcube = net.copy()
    cubelen = net.shape[0]

    for z in range(cubelen):
        printLayer(z, net)


    for iz in range(cubelen):
        if(iz == 1 and ignoreCfgLayer):
            continue

        for iy in range(cubelen):
            for ix in range(cubelen):

                node = getpos(ix, iy, iz, net)
                activeCount, checkdCount = countaround(ix, iy, iz, net)
                newnode = node

                if( node == 1 and not activeCount in [2, 3] ):
                    newnode = 0
                if( node == 0 and activeCount == 3 ):
                    newnode = 1

                setpos(ix, iy, iz, newnode, newcube)

                print(f"{c=} : {ix=} {iy=} {iz=} / {cubelen=} : {checkdCount=} : {activeCount=} {node=} {newnode=} : {activeCount in [2,3]=}")
            print("")


        # Print the new layers
        print("orig", end=" ")
        printLayer(iz, net)
        print("new", end=" ")
        printLayer(iz, newcube)
    #print(newcube)

    print("New cycle\n")
    net = newcube

    return runCycle(net, c+1, expand=True, ignoreCfgLayer=ignoreCfgLayer)

# print("###################################")
# cube, cubelen = expandCube(cube, 10)
# endcube = runCycle(cube)
# print(endcube)
# print( np.sum(endcube) )

cycles = 6
def runCycle4(net, c=0, maxc=cycles, expand=False):
    if( not c < maxc ):
        print("Done")
        return net

    if(expand):
        net, cubelen = expandCube(net, 1)
    newcube = net.copy()
    cubelen4 = net.shape[0]

    for iw in range(cubelen4):
        for iz in range(cubelen4):

            for iy in range(cubelen4):
                for ix in range(cubelen4):

                    node = getpos4(ix, iy, iz, iw, net)
                    activeCount, checkdCount = countaround4D(ix, iy, iz, iw, net)
                    newnode = node

                    if( node == 1 and not activeCount in [2, 3] ):
                        newnode = 0
                    if( node == 0 and activeCount == 3 ):
                        newnode = 1

                    setpos4(ix, iy, iz, iw, newnode, newcube)

                    #print(f"{c=} : {ix=} {iy=} {iz=} {iw=} / {cubelen4=} : {checkdCount=} : {activeCount=} {node=} {newnode=} : {activeCount in [2,3]=}")
                #print("")


            # Print the new layers
            #print("orig", end=" ")
            #printLayer(iz, net)
            #print("new", end=" ")
            #printLayer(iz, newcube)

    #print(newcube)

    #print("New cycle\n")
    print(c, "/", maxc)
    net = newcube

    return runCycle4(net, c+1, expand=True)

cube4, cubelen4 = expandCube(cube4, 2)
endcube4 = runCycle4(cube4)
print(endcube4)
print( np.sum(endcube4) )
