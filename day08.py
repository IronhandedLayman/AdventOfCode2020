#!/usr/bin/env python3

DAY=8

def dataLocation(day):
    return "data/day{:02d}-data.txt".format(day)

def loadData(day):
    ans=""
    with open(dataLocation(day),"r") as fh:
        ans=fh.read()
    return [ln.strip() for ln in ans.split("\n") if len(ln.strip())>0]

def parseAsm(asmlines):
    return [parseAsmLine(x) for x in asmlines]

def parseAsmLine(asmline):
    inst, arg = asmline.split(" ")
    return (inst.strip(), int(arg))

def runInfProg(program, acc, flipinst=-1):
    pc=0
    visited=set()
    while pc>=0 and pc<len(program) and pc not in visited:
        visited.add(pc)
        pc, acc = runClock(program,pc,acc, flipinst==pc)
    return (acc, pc in visited)

def runClock(program,pc,acc, flipinst):
    instr = program[pc]
    if instr[0] == "nop" or (instr[0]=="jmp" and flipinst):
        return (pc+1,acc)
    elif instr[0] == "acc":
        return (pc+1,acc+instr[1])
    elif instr[0] == "jmp" or (instr[0]=="nop" and flipinst):
        return (pc+instr[1],acc)
    return (pc+1,acc)

def star1():
    ans = 0
    prog = parseAsm(loadData(DAY))
    ans, fc = runInfProg(prog,ans)
    return ans

def star2():
    ans = 0
    prog = parseAsm(loadData(DAY))
    for cc in range(len(prog)):
        if prog[cc][0]=="acc":
            continue
        else:
            ans, fc = runInfProg(prog, 0,cc)
            if not fc:
                return ans
    return ans
