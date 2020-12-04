#!/usr/bin/env python

from aoc import get_input

import re

inp = get_input(4)

newPort = "\n\n"

validPara = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"] # NOTE excluade cid later


ports = inp.split(newPort)

def getPorts(port):
    port = port.replace("\n", " ")

    paras = port.split(" ")
    out = []
    #print("####", paras)

    for p in paras:
        #print("#",p)
        if( p != "" ):
            para = re.match("(\w+):", p).groups()[0]
            out.append(para)

    return out

def checkPorts(ports, valids, ignore:list = ["cid"]):
    paras = []
    for p in ports:
        paras.append(getPorts(p))

    count = 0

    for para in paras:
        check = all(p in para  for p in valids)
        print(check, para, valids)
        if(check):
            count += 1

    return count

            

specialPara =  ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# pcheck = checkPorts(ports, specialPara)


# print(pcheck)

def getPortsYes(port):
    port = port.replace("\n", " ")

    paras = port.split(" ")
    out = []

    for p in paras:
        if( p != "" ):
            val = re.split(":", p)[1]
            para = re.match("(\w+)\:", p).groups()[0]
            out.append([para, val])

    return out


eyecolors = "amb blu brn gry grn hzl oth".split(" ")

def checkVal(par, val):
    valid = True
    if( par == "byr" ):
        valid = int(val) <= 2002 and int(val) >= 1920
        print("byr", int(val), valid)

    elif( par == "iyr" ):
        valid = int(val) <= 2020 and int(val) >= 2010
        print("iyr", int(val), valid)

    elif( par == "eyr" ):
        valid = int(val) <= 2030 and int(val) >= 2020
        print("eyr", int(val), valid)

    elif( par == "hgt" ):
        num, typ = re.match("(\d+)(\w+)", val).groups()
        if( typ == "cm" ):
            valid = int(num) <= 193 and int(num) >= 150
            print("hgt cm", int(num), valid)
        elif( typ == "in" ):
            valid = int(num) <= 76 and int(num) >= 59
            print("hgt in", int(num), valid)
        else:
            valid = False

    elif( par == "hcl" ):
        try:
            string = val.split("#")[1]
            check1 = len(string) == 6
            validhex = re.search("^([a-fa-f0-9]{6})$", string)
            print("hcl", val, len(string), check1, validhex)
            if( not validhex ):
                valid = False
        except:
            valid = False

    elif( par == "ecl" ):
        valid = val in eyecolors
        print( "ecl", val, eyecolors, valid )

    elif( par == "pid" ):
        try:
            num = int(val)
            check = len(val) == 9
            valid = check
            print("pid", num, len(val), val, check)
        except:
            valid = False
    elif( par == "cid" ):
        valid = True

    else:
        valid = False



    return valid

def checkPortsVALID( ports, paras ):
    count = 0


    for port in ports:
        ps = getPortsYes(port)
        parasPort = getPorts(port)
        portsValid = True
        portsValid2 = True

        #for para in ps2:

        check2 = all(p in parasPort  for p in paras)
        if( not check2 ):
            print("FALSE:", parasPort, "####", paras )
            portsValid2 = False

        for p in ps:
            if(p != ""):
                param = p[0]
                val = p[1]
                #print("|<", param, val)

                check1 = checkVal(param, val)


                #print(check2)

                if(check1 == False):
                    portsValid = False


        if( portsValid == True and portsValid2 == True ):
            count += 1

        print("\nnewport")

    return count

check1 = checkPorts(ports, specialPara)
pcheck2 = checkPortsVALID( ports, specialPara )

print("Part2:", check1, pcheck2)
