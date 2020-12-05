#!/usr/bin/env python3

import re

DAY=4

PP_PAT=re.compile("([a-z]{3}):(.*?)[ \n]")
COL_PAT=re.compile("^#[0-9a-f]{6}$")
SET_REQ=set(["byr","iyr","eyr", "hgt", "hcl", "ecl", "pid"])

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return [ln.replace("\n"," ") for ln in ans.split("\n\n")]

def star1():
    inp = loadData(DAY)
    ans=0
    print(len(inp))
    for pp in inp:
        bd = [x for m in PP_PAT.finditer(pp+" ") for x in [m.groups()]]
        hf = set([k[0] for k in bd])
        if SET_REQ.issubset(hf):
            for (k,v) in bd:
                if k=='byr' and (len(v)!=4 or 1920>int(v) or int(v)>2002):
                    print("-----fail birthyear", v)
                    break
                if k=='iyr' and (len(v)!=4 or 2010>int(v) or int(v)>2020):
                    print("-----fail issue year", v)
                    break
                if k=='eyr' and (len(v)!=4 or 2020>int(v) or int(v)>2030):
                    print("-----fail expiration year", v)
                    break
                if k=='hgt':
                    if v.endswith("in"):
                        inh=int(v[:-2])
                        if len(v)!=4 or 59>inh or inh>76:
                            print("-----fail inch height", inh)
                            break
                    elif v.endswith("cm"):
                        inh=int(v[:-2])
                        if len(v)!=5 or 150>inh or inh>193:
                            print("-----fail cm height", inh)
                            break
                    else:   
                        print("-----fail in or cm height", v)
                        break
                if k=='hcl' and COL_PAT.match(v) is None:
                    print("-----fail hair color", v)
                    break
                if k=='ecl' and (len(v)!=3 or v not in "amb blu brn gry grn hzl oth".split(" ")):
                    print("-----fail eye color", v)
                    break
                if k=='pid' and re.compile("^[0-9]{9}$").match(v) is None:
                    print("-----fail passport id", v)
                    break
            else:
                print(pp)
                print("-----pass")
                ans+=1
        else:
            print("-----fail subsets")
    return ans

def star2():
    inp = loadData(DAY)
    return -1
