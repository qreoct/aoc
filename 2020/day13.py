time, buses = open("day13.txt").read().splitlines()
buses = buses.strip().split(",")

def gcd(a,b):
    if b == 0: return a
    else: return gcd(b, a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def offset(xs): # turns the list of "1,x,99,88" into a dictionary of {bus: offset}, i.e. {1: 0, 99: 2, 88: 3}
    res = {} 
    for i in range(len(xs)):
        if xs[i] == "x": pass
        else: res[int(xs[i])] = i
    return res


# part1
import math
start = int(time)
min_so_far = math.inf 
ans = 0
for bus in buses:
    if bus == "x":
        pass
    else:
        bus = int(bus)
        a = start-(start//bus+1)*bus # bruteforce stuff.. find the closest to the start then get the smallest diff
        if abs(a) < min_so_far:
            min_so_far = abs(a)
            ans = abs(a) * bus
print('silver:', ans)

# part2

from functools import reduce
buses = offset(buses) # read offset function for what this does

found = False
all_buses = [b for b in buses][1:]
curr = [[b for b in buses][0]]
t = 0

while not found: #apparently recursion is too much for the stack so we do it iteratively
    # logic: only increment in steps of lcm of what we have seen before
    # you only have to check the divisibility of the last number

    # e.g. 17,x,13,19
    # 0%17 == 0 is satisfied, so t = 0
    # next increment by lcm(17), until t+2%13 == 0 is satisfied
    # this happens at t = 102
    # next increment by lcm(17,13) until t+3%19 == 0 is satisfied
    # this happens at t = 3417 which is our solution

    # TODO: this is basically chinese remainder theorem with setting up a system of congruences
    
    lc = reduce(lcm, curr[:-1]) if len(curr) != 1 else curr[0]
    bus = curr[-1]
    if (t+buses[bus])%bus == 0:
        if all_buses == []:
            found = True
            print('gold:', t)
        else:
            curr.append(all_buses[0])
            all_buses = all_buses[1:]
    else:
        t += lc 


