#!/usr/bin/env python3

DAY=1

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return ans

def star1_sumto2020():
    procData=[int(x) for x in loadData(DAY).split("\n") if len(x)>0]
    fatedPair=[(x,y) for x in procData for y in procData if x+y==2020][0]
    return fatedPair[0]*fatedPair[1]
