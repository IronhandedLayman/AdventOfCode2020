#!/usr/bin/env python3

from functools import reduce
# import re

DAY=3

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return ans

def star1_watch_out_for_that():
    return count_slope(3,1)

def count_slope(dx, dy):
    treefield = [ln for ln in loadData(DAY).split("\n") if len(ln)>0]
    treecount = 0
    xpos,ypos = 0,0
    while ypos < len(treefield):
        print(xpos, ypos)
        if treefield[ypos][xpos]=='#':
            treecount+=1
        xpos = (xpos+dx) % len(treefield[0])
        ypos += dy 
    return treecount

def star2_plan_ahead():
    slopecounts = [count_slope(xx,yy) for xx,yy in [(1,1),(3,1),(5,1),(7,1),(1,2)]]
    return reduce(lambda x,y:x*y,slopecounts)
