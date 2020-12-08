#!/usr/bin/env python3

import re

DAY=7
BAG_PARSE = re.compile("([0-9]+ )?([a-z]+ [a-z]+) bag")

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return [ln.strip() for ln in ans.split("\n") if len(ln.strip())>0]

def processBagRule(bagRule):
    lside, rside = bagRule.split(" contain ")
    lbag = processBag(lside)
    rbags = processBagList(rside)
    return (lbag,rbags)

def processBagList(baglist):
    return [processBag(x) for x in baglist.split(",")]

def processBag(bagtype):
    gr = BAG_PARSE.search(bagtype)
    if gr is None or gr[2].strip()=="no other":
        return {"count":0, "type":"None"}
    if gr[1] is None:
        return {"count":0, "type":gr[2].strip()}
    return {"count":int(gr[1]), "type":gr[2].strip()}


def updownTree(bagrules_text):
    ruleTree = {}
    reverseTree = {}
    for br_text in bagrules_text:
        try:
            lbag, rbags = processBagRule(br_text)
        except:
            print("failed parsing on: {}".format(br_text))
        lb_type = lbag["type"]
        ruleTree[lb_type] = rbags
        for x in rbags:
            if x["type"]=="None":
                continue
            if (bt:=x["type"]) in reverseTree:
                reverseTree[bt].append(lb_type)
            else:
                reverseTree[bt] = [lb_type]
    return ruleTree,reverseTree

def star1():
    ruleTree,reverseTree = updownTree(loadData(DAY))
    ans = 0
    sans = set() 
    upsearch = ["shiny gold"]
    while len(upsearch) > 0:
        cur = upsearch.pop(0)
        # print("searching: {}".format(cur))
        if cur not in reverseTree:
            continue
        for x in reverseTree[cur]:
            if x not in sans:
                sans.add(x)        
                upsearch.append(x)
    return len(sans)

def bagcount(bagname,ruleTree,reverseTree):
    # print("entering bagcount for {}".format(bagname))
    if bagname not in ruleTree:
        return 0
    ans = 1
    for x in ruleTree[bagname]:
        if x["type"]=="None":
            continue
        ans += x["count"]*bagcount(x["type"],ruleTree,reverseTree)
    # print("bagcount for {} is {}".format(bagname,ans))
    return ans

def star2():
    ruleTree,reverseTree = updownTree(loadData(DAY))
    return bagcount("shiny gold",ruleTree,reverseTree)-1 #not the bag itself LOL 
