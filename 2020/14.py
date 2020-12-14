#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex
import itertools as it

data = get_input(14).splitlines()

def listToString(s):

    str1 = ""
    for ele in s:
        str1 += ele

    return str1

def dectobin(num):
    return format(num, "036b")

def bintodec(_bin):
    return int(_bin, 2)

def parseLine(line):
    if( line[0:3] == "mem" ):
        address, val = re.match( r"^mem\[([0-9]+)\] = ([0-9]+)$", line ).groups()
        _bin = dectobin(int(val))

        return address, _bin

    else:
        op, mask = line.split(" = ")
        return op, mask

def applyMask( _bin, mask ):
    newbin = []
    newbin[:0] = _bin

    for i in range(len(mask)):
        if( mask[i] != "X" ):
            newbin[i] = mask[i]

    return listToString(newbin), _bin

def applyMask2( addr, mask ):
    newaddr = []
    newaddr[:0] = addr

    print(addr, len(addr))

    for i in range(len(mask)):
        newaddr[i] = mask[i]

    return listToString(newaddr)


def copyList(lst):
    return [elem  for elem in lst]

def getallcombs(xlen):
    return [list(i) for i in it.product(["0", "1"], repeat=xlen)]

def getAddressCombos(mask, addr):
    addrlist = []
    addrlist[:0] = addr
    xlen = mask.count("X")

    combs = getallcombs(xlen)

    addrcombos = []

    for comb in combs:
        xcount = 0
        newaddrlist = copyList(addrlist)
        for i in range( len(newaddrlist) ):
            char = newaddrlist[i]
            maskchar = mask[i]

            if(maskchar == "X"):
                newaddrlist[i] = comb[xcount]
                xcount += 1
            elif(maskchar == "1"):
                newaddrlist[i] = maskchar

        addrcombos.append( listToString(newaddrlist) )

    return addrcombos


# Part 1 & 2

curMask = None
mem = dict()
mem2 = dict()

for line in data:
    address, val = parseLine(line)
    if( address != "mask" ):
        val, oldval = applyMask(val, curMask)
        dec_val, dec_oldval = bintodec(val), bintodec(oldval)

        mem[address] = dec_val

        # apply mask to address
        address = dectobin(int(address))
        addrlist = getAddressCombos(curMask, address)

        for addr in addrlist:
            decaddr = bintodec(addr)
            mem2[decaddr] = bintodec(val)

    else:
        curMask = val
        continue

memsum, memsum2 = sum(mem.values()), sum(mem2.values())

print("Part1:", memsum)
print("Part2:", memsum2)
