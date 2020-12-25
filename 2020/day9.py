f = list(map(int, open("day9.txt").read().splitlines()))

def xmas_valid(xmas, preamble, point, segment): #will go through the entire xmas list until an invalid entry. will return the invalid entry and the position.
    nxt = xmas[point+preamble]
    if valid_next(nxt, segment): return xmas_valid(xmas, preamble, point+1, xmas[point+1: point+1+len(segment)])
    else:
        print('nxt is invalid: ', nxt, 'at position ', point)
        return nxt, point

def valid_next(nxt, prevs): #checks if the next number in the list can be obtained by a sum of 2 elements in the prevs list
    for a in prevs:
        for b in prevs:
            if a+b == nxt: return True
    return False
begin = time.time()
invalid, invalid_pos = xmas_valid(f, 25, 0, f[0:25]) #preamble length is the 2nd param and the 4th param
#part1
print('silver:', invalid)

#part2
def find_contig(remain_sum, remain, acc): #returns list of contiguous numbers from index 0 to i of list of n elements that sum to remain_sum. if no list can be found, return False
    if remain_sum == 0 : return acc
    elif (len(remain) <= 1 or remain_sum < 0): return False
    else:
        r = remain[0]
        acc.append(r)
        return find_contig(remain_sum - remain[0], remain[1:], acc)

for i in range(invalid_pos):
    ans = find_contig(invalid, f[i:invalid_pos], [])
    if ans == False : pass
    else:
        print('gold:', min(ans) + max(ans))

