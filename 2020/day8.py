f = open("day8.txt").read().splitlines()

def follow_inst(point, acc, insts, done, part1):
    if point in done: 
        if part1: print("silver:",acc) #have to print the last acc value for part1
        return -1
    elif point >= len(insts):
        print("gold:", acc) #only print the last acc value if it terminates
        return acc
    inst = insts[point]

    op = inst.split(" ")[0]
    amt = inst.split(" ")[1]
    amt = int(amt[1:]) if amt[0] =="+" else -int(amt[1:])
    done.append(point)
    if op == "nop":
        return follow_inst(point+1, acc, insts, done, part1)
    elif op == "acc":
        return follow_inst(point+1, acc+amt, insts, done, part1)
    else:
        return follow_inst(point + amt, acc, insts, done, part1)

#part1
follow_inst(0,0,f,[], True) #single line: infinite: xxx

#part2
#bruteforce replace each jmp with nop and vice versa, then run the program to check

pnt = 0
for i in f:
    if i[0:3]=="jmp":
        cp = f.copy()
        cp[pnt] = cp[pnt].replace("jmp","nop")
        ans = follow_inst(0,0,cp,[], False)
        if ans !=-1: break
        elif i[0:3]=="nop":
            cp = f.copy()
            cp[pnt] = cp[pnt].replace("nop","jmp")
            ans = follow_inst(0,0,cp,[], False)
            if ans != -1: break
        else: pass
        pnt+=1
