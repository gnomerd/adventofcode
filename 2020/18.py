#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex

mathproblems = get_input(18).splitlines()

operators = ["+", "*"]

def strToList(string):
    list1=[]
    list1[:0]=string
    return list1

def findParens(s):
    toret = dict()
    pstack = []

    for i, c in enumerate(s):
        if( c == "(" ):
            pstack.append(i)
        elif( c == ")" ):
            if( len(pstack) == 0 ):
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if(len(pstack) > 0):
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret

def getFirstNum(chars:list):
    first = None

    for i in range(len(chars)):
        char = chars[i]
        print(f"check {char=}", end=" ")
        if(not char in operators and char != "(" and char != ")" and char != ""):
            first  = int(char)
            print("is first")

            break
        else:
            print("")

    return first


def calcMath(chars:list):
    count = 0
    first = getFirstNum(chars)
    count += first

    for i in range(len(chars)):
        char = chars[i]

        after = None

        if(char == "+"):
            after = chars[i+1]
            count += int(after)
        elif(char == "*"):
            after = chars[i+1]
            count *= int(after)

        print(f"{first=} {char=} {i=} {after=} {count=}")

    return count

def parseMath(line):
    line =  line.replace(" ", "")
    count = 0

    # calculate all pars  and replace them
    pars = findParens(line)
    chars = strToList(line)
    print(chars)

    for start, end in pars.items():
        calc = calcMath(chars[start:end+1])

        for j in range(start, end+1):
            chars[j] = ""

        chars[start] = str(calc)


    print("##########3")
    # remove bad chars
    chars = list( filter(lambda c: c != "", chars) )
    print(chars)


    # calculate the rest
    count += calcMath(chars)

    return count

def printMath(mathlist):
    for m in mathlist:
        print(m, end="")
    print("")

def lstToStr(lst):
    out = ""
    for char in lst:
        out += str(char)
    return out

def copyList(lst):
    return [elem  for elem in lst]

# def addPars(line:str):
#     chars = strToList(line)
#     plusCount = chars.count("+")

#     seekingEnd = None
#     parsPos = dict()

#     print("#", line)
#     for i in range(len(chars)):
#         char = chars[i]

#         if(char == "+"):
#             parsPos[i-1] = None
#             seekingEnd = i-1

#         if( (char == "*" and seekingEnd != None) ):
#             parsPos[seekingEnd] = i
#             seekingEnd = None

#         if( seekingEnd != None and i >= len(chars) - 1 ):
#             parsPos[seekingEnd] = i+1
#             seekingEnd = None

#         if( seekingEnd != None and char == ")" ):
#             parsPos[seekingEnd] = i+1
#             seekingEnd = None

#         print(f"{i=}:{char=} {parsPos=}")

#     offset = 0
#     needEnd = 0
#     for pstart, pend in parsPos.items():
#         print("#", pstart, pend)

#         if(pend != None):
#             chars.insert(pstart+offset, "(")
#             offset += 1

#             chars.insert(pend+offset, ")")
#             offset += 1
#         else:
#             chars.insert(pstart+offset, 0)
#             offset += 1
#             printMath(chars)

#             chars.insert(pstart+offset, "+")
#             offset += 1
#             printMath(chars)

#             chars.insert(pstart+offset-2, "(")
#             offset += 1
#             printMath(chars)

#             needEnd += 1

#     for i in range(needEnd):
#         chars.append(")")

#     print("RES", end=" ")
#     printMath(chars)

#     return chars

# import ast

# def recurse(node):
#     out = ""
#     if( isinstance(node, ast.Add) ):


# def addPars(line:str):
#     out = strToList(line)

#     offset = 0
#     parDepth = 0
#     seekingClose = False

#     startFound = None
#     endFound = None

#     for i in range(len(line)):
#         char = line[i]
#         prefix = "-----"

#         if( char == "+" and not seekingClose ):
#             out.insert(i - 1 + offset, "(" )
#             seekingClose = True
#             startFound = i-1+offset
#             offset += 1


#             prefix = "start"

#         elif( char == "(" ):
#             parDepth += 1
#         elif( char == ")" ):
#             parDepth -= 1

#         elif( (char == "*") and seekingClose and parDepth == 0 ):
#             out.insert(i + offset, ")")
#             offset += 1
#             seekingClose = False
#             endFound = i+offset

#             prefix = "close"



#         math = lstToStr(out)
#         print(f"{prefix} {i=}:{char=} {math=} {offset=}")

#     return out

def addParsToSub(line:str):
    # this function split the strings addition thing
    # no parenthesis here

    addlines = line.split("*") # each element is an addition
    newline = ""

    for i in range(len(addlines)):
        l = addlines[i]
        if( i < 1 ):
            newline += f"({l})*"
        elif( i >= 1 and i < len(addlines)-1 ):
            newline += f"({l})*"
        elif( i == len(addlines)-1 ):
            newline += f"({l})"

    return newline

    
def parseMath2(line):
    line = line.replace(" ", "")
    count = 0




problem = mathproblems[0]
res = parseMath2(problem)
print("\n--##########################--")
print( problem, "=", res )

# mathsum = 0

# for maththing in mathproblems:
#     mathsum += parseMath(maththing)

# print(mathsum)
