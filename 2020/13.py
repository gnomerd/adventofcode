#!/usr/bin/env python

from aoc import get_input # AoC
import re # regex

data = get_input(13).splitlines()

time = int(data[0])

busses = []
for busid in data[1].split(","):
    if(busid != "x"):
        busses.append(int(busid))
    # else:
    #     busses.append(busid)

##busses.sort()


def getTimestamp(busid, i):
    return busid * i


# bustimes = dict()

# for busid in busses:
#     print("checking ", busid)
#     i = 0
#     bustimes[busid] = []
#     while True:
#         timestamp = getTimestamp(busid, i)
#         bustimes[busid].append(timestamp)

#         if(timestamp > time):
#             break
#         else:
#             i += 1
#             continue

# waittimes = dict()
# for busid, t in bustimes.items():
#     high = max(t)
#     waittimes[busid] = high - time

# bestbusid = min(waittimes, key=waittimes.get)

# thing = bestbusid * waittimes[bestbusid]

# print(bestbusid, thing)


bus = dict()
i = 0
for busid in data[1].split(","):
    if(busid != "x"):
        bus[i] = int(busid)

    i += 1


minindex, maxindex = 0, len(bus) - 1
from sympy.ntheory.modular import crt

thing = []
buss = []
for i, busid in bus.items():
    thing.append(i)
    buss.append(busid)

print(bus, buss, thing)
hello = crt(buss, thing)
print(hello)

thething = hello[1] - hello[0]
print(thething)
