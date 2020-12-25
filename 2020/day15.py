f = [int(x) for x in open("day15.txt").read().split(',')]

def solve(turns):
    mem = [(0,0)]*turns # van eck's sequence at position n is guaranteed to be < n, so can initialize array to be turns size 
                        # because of that, we can also use an array as the hashmap itself. saves maybe a bit of time
    last = f[0]
    for i in range(turns):
        if i < len(f):
            mem[f[i]] = (mem[f[i]][1], i+1) 
            last = f[i]
        else:
            recent = mem[last] #are you able to find the last number spoken in the mem?
            if recent[0] == 0:
                mem[0] = (mem[0][1], i+1)
                last = 0
            else:
                last = recent[1] - recent[0]
                mem[last] = (mem[last][1], i+1)

    return last

import time

s = time.time()
print('silver: ', solve(2020))
print('time: {} seconds'.format(time.time() - s))

g = time.time()
print('gold: ', solve(30000000))
print('time: {} seconds'.format(time.time() - g))

