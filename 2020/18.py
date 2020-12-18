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



# def addParsToSub(line:str):
#     # this function split the strings addition thing
#     # no parenthesis here

#     addlines = line.split("*") # each element is an addition
#     #newline = "("
#     newline = ""

#     for i in range(len(addlines)):
#         l = addlines[i]
#         if( i < 1 ):
#             newline += f"({l})*"
#         elif( i >= 1 and i < len(addlines)-1 ):
#             newline += f"({l})*"
#         elif( i == len(addlines)-1 ):
#             newline += f"({l})"

#     #newline += ")"

#     return newline


# def getLowestPar(par:dict):
#     bestdiff = None
#     bestkey = None

#     for key, val in par.items():
#         diff = val - key

#         if( bestdiff == None ):
#             bestdiff = diff
#             bestkey = key
#             continue

#         if( diff > bestdiff ):
#             bestdiff = diff
#             bestkey = key
#             continue

#     return bestkey



# def addPars(line:str, usedPar=[]):
#     line = line.replace(" ", "")
#     newline = line
#     count = 0

#     # Get pars etc
#     pars = findParens(line)
#     chars = strToList(line)

#     print(pars)

#     # Get pars with lowest depth
#     start = getLowestPar(pars)
#     end = pars[start]+1


#     # Enclose addition in pars
#     subline = lstToStr(chars[start:end])
#     newsubline = addParsToSub(subline)

#     newline = newline.replace(subline, newsubline)

#     # for start, end in pars.items():
#     #     if( not start in usedPar ):
#     #         x, y = start, end+1
#     #         subline = lstToStr(chars[x:y])
#     #         newsubline = addParsToSub(subline)

#     #         newline.replace(subline, newsubline)
#     #         print(f"{newsubline=}")

#     print("FINAL", newline)
#     print(subline, newsubline)
#     print(addParsToSub(newline))

# def addParsRec(line:str, usedPar=[]):
#     line = line.replace(" ", "")
#     newline = line

#     pars = findParens(newline)


# def addParsRec(line:str, i=0, it=None):
#     it = it or line.count("(")

#     if( i < it ):
#         return addParsRec( addParsToSub(line), i+1, it )
#     else:
#         return line


def addPars(chars:list):
    curDepth = 0
    addDepth = 0

    isSearching = False

    offset = 0
    for i, char in enumerate(chars):
        if( char == "(" ):
            curDepth += 1
        elif( char == ")" ):
            curDepth -= 1

        if( char == "+" ):
            before = chars[i-1+offset]
            # if(before == ")" or before == "("):
            #     chars.insert(i+offset, "0")
            #     offset += 1

            curDepthSec = curDepth
            for di, char2 in enumerate(chars[i+1:]):

                if( char2 == "(" ):
                    curDepthSec += 1
                    continue
                elif( char2 == ")" ):
                    curDepthSec -= 1

                if( curDepthSec != curDepth ):
                    continue

                print(f"{i=} : {di+1+offset=} {char=} {char2=} {curDepth=} : {curDepthSec=}")

                if( char2 == "*" and curDepth == curDepthSec ):
                    chars.insert(i+offset+di, ")")
                    offset += 1



        # if( char == "+" and not isSearching ):
        #     chars.insert(i-1+offset, "(")
        #     addDepth = curDepth
        #     isSearching = True
        #     offset += 1

        # elif( char == "*" and curDepth == addDepth ):
        #     chars.insert(i+offset, ")")

    return chars

class Fusk(int):
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Fusk(self.value + other.value)

    def __sub__(self, other):
        return Fusk(self.value * other.value)


def parseMath2(line:str):
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


# problem = mathproblems[0]
# print(problem.replace(" ", ""))
# newprob = problem.replace(" ", "")

# probList = addPars( strToList(newprob) )
# newprob = lstToStr(probList)

#print(newprob)
# res = parseMath2(problem)
# print("\n--##########################--")
# print( problem, "=", res )

mathsum, mathsum2 = 0, 0

for maththing in mathproblems:
    mathsum += parseMath(maththing)

    x = str.maketrans({"*": "-", "+": "*"})
    trans = maththing.translate(x)
    print("##############", x, trans)

    maththing = re.sub( r"([0-9]+)", r"Fusk(\1)", trans )
    print(maththing)
    mathsum2 += eval(maththing)

print(mathsum, mathsum2)
