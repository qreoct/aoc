f = sorted(list(map(int, open("day10.txt").read().splitlines())))
print(f)

count1 = 0
count3 = 0
last = 0
for i in f:
    if i-last == 1 : count1 += 1
    elif i-last == 3 : count3 += 1
    last = i


print('silver:', count1*(count3+1))

#part2
# some rules: the last guy must always be included
# you probably can start by taking first, or second, or third, and then recursively work on the sublist
from itertools import permutations
import copy

def dist_3_pairs(xs):
    pairs = []
    for i in range(len(xs)-1):
        if xs[i+1] - xs[i] == 3: pairs.append((i, i+1))
    return pairs

pairs = dist_3_pairs(f)
diffs = []

for i in range(len(pairs)+1):
    if i == 0: diffs.append(f[0 : pairs[i][1]-1])
    elif i == len(pairs): diffs.append(f[pairs[i-1][1]+1:len(f)-1])
    else:
        diffs.append(f[pairs[i-1][1]+1 : pairs[i][0]])

acc = 1
for d in diffs:
    if len(d) == 0: acc *= 1
    elif len(d) == 1: acc *= 2
    elif len(d) == 2: acc *= 4
    elif len(d) == 3: acc *= 7

print('gold: ', acc)
    



