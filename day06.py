#!/usr/bin/env python3

DAY=6

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return [ln.strip().split("\n") for ln in ans.split("\n\n")]

def star1():
    inp = loadData(DAY)
    ans = 0
    for gr in inp:
        print(gr)
        aa = {}
        for fl in gr:
            for qu in fl:
                aa[qu] = True
        print(aa, [k for k in aa])
        ans += len([k for k in aa])
    return ans

def star2():
    inp = loadData(DAY)
    ans = 0
    for gr in inp:
        print(gr)
        aa = {}
        for fl in gr:
            for qu in "abcdefghijklmnopqrstuvwxyz":
                if qu not in fl:
                    aa[qu] = True
        print(aa, [k for k in aa])
        ans += 26-len([k for k in aa])
    return ans
