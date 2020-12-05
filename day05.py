#!/usr/bin/env python3

DAY=5

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return [ln.strip() for ln in ans.split("\n") if len(ln)>0]

def translateRow(bp):
    return int(bp.replace("F","0").replace("B","1").replace("R","1").replace("L","0"),2)

def star1():
    inp = loadData(DAY)
    ans = max([translateRow(x) for x in inp])
    return ans

def star2():
    inp = loadData(DAY)
    allseats = sorted([translateRow(x) for x in inp])
    poss = [x for x in range(min(allseats),max(allseats)+1) if x not in allseats and (x-1) in allseats and (x+1) in allseats]
    ans = min(poss)
    return ans

def testTranslateRow():
    """
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    """
    if (cv := translateRow((tv:="BFFFBBFRRR"))) != (ev:=567):
        print("fail: translateRow({}) != {} but == {}".format(tv,ev,cv))
    elif (cv := translateRow((tv:="FFFBBBFRRR"))) != (ev:=119):
        print("fail: translateRow({}) != {} but == {}".format(tv,ev,cv))
    elif (cv := translateRow((tv:="BBFFBBFRLL"))) != (ev:=820):
        print("fail: translateRow({}) != {} but == {}".format(tv,ev,cv))
    else:
        print("PASS")
