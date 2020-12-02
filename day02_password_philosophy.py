#!/usr/bin/env python3

# from functools import reduce
import re

DAY=2

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return ans

def star1_valid_passwords():
    pwlist = loadData(DAY).split("\n")
    parser = re.compile("^([0-9]+)-([0-9]+) ([a-z]): (.*)$") 
    validCount = 0
    for pwline in pwlist:
        try:
            le, he, let, pw = parser.match(pwline).groups()
            lei, hei = int(le), int(he)
            letCount = len([a for a in pw if a==let[0]])
            if lei<=letCount and letCount<=hei:
                validCount+=1
                print("{} has {} {}'s, which is between {} and {}".format(pw, letCount, let, lei, hei))
        except:
            pass
    return validCount
