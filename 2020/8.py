#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex
from copy import copy

CodeLines = get_input(8).splitlines()
print(CodeLines)

def parseCode(code):
    if( code and code != "" ):
        regex = r"^([a-z]{3}) ([\+\-]{1})([0-9]+)$"
        op, sign, num = re.match(regex, code).groups()

        return op, sign, int(num)
    else:
        print("INVALID CODE:", code)
        return


accu = 0
line = 0

def runCode(op, sign, num, newline=line, newaccu=accu):
    if( op == "nop" ):
        newline += 1
    elif( op == "acc" ):
        if( sign == "+" ):
            newaccu += num
        elif( sign == "-" ):
            newaccu -= num

        newline += 1
    elif( op == "jmp" ):
        if( sign == "+" ):
            newline += num
        elif( sign == "-" ):
            newline -= num

    return newline, newaccu


def swapCode(line, codes):
    op, sign, num = parseCode(codes[line])
    newcode = ""

    if( op == "nop" ):
        newcode = f"jmp {sign}{num}"
    elif( op == "jmp" ):
        newcode = f"nop {sign}{num}"
    else:
        return codes[line]

    return newcode


def runProgram(codes=CodeLines, i=0, linefix=None, linecode=None, oldline=None):
    print(f"\nRunning program iter:{i}")
    print(f"Codes: {codes}")
    seenLines = []
    codeLen = len(codes)

    line = 0
    accu = 0

    loop = False

    while True:
        try:
            if( not loop ):
                if( line < codeLen ):
                    code = codes[line]
                    op, sign, num = parseCode(code)

                    newline, newaccu = runCode(op, sign, num, line, accu)

                    print(f"op:{op} num:{sign}{num} line:{line}/{codeLen} newline:{newline}/{codeLen} accu:{accu} newaccu:{newaccu}")

                    if(newline in seenLines):
                        print(f"REPEAT AT: line:{line} newline:{newline} newaccu:{newaccu} seenLines:{seenLines}")

                        if( op == "jmp" ):
                            loop = True
                            print("LOOP")

                    seenLines.append(newline)
                    accu = newaccu
                    line = newline

                else:
                    print("END OF PROGRAM")
                    print(accu, line)
                    return accu, line, codeLen
            else:
                print("BAD LOOP")
                break
        except:
            print(f"ERROR line:{line} maxline:{codeLen}")
            print(accu)
            return accu, line, codeLen

count = 0

jmpThings = dict()

for l in range(len(CodeLines)):
    code = CodeLines[l]
    newcodes = CodeLines
    op, sign, num = parseCode(code)

    if( op == "nop" or op == "jmp" ):
        jmpThings[l] = (op, sign, num)

print(jmpThings) # Need to change one of these

for codeline, ins in jmpThings.items():
    print("\n\n####")
    newcodes = copy(CodeLines)
    newcodes[codeline] = swapCode(codeline, CodeLines)
    print(f"newcodes:{newcodes} | {newcodes[codeline]}")
    print(f"oldcodes:{CodeLines} | {CodeLines[codeline]}")

    out = runProgram(newcodes)
    print(f"OUT:{out}")
    if( out ):
        print("############ OUT:", out)
        break
    else:
        continue
