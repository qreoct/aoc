f = open("day11.txt").read().splitlines()
from copy import deepcopy

# making the floor array from input
# access values with floor[y-coord][x-coord]
floor = []
for i in range(len(f)):
    line = []
    for s in range(len(f[i])):
        line.append(f[i][s])
    floor.append(line)

def checkseat(i,j,floor): # really ugly... returns number of occupied adjacent seats with boundary checking
    w = west(i,j)
    w = "0" if w[1] < 0 else floor[w[0]][w[1]] # out of bounds else correct
    e = east(i,j)
    e = "0" if e[1] >= len(floor[0]) else floor[e[0]][e[1]] # out of bounds else correct
    n = north(i,j)
    n = "0" if n[0] < 0 else floor[n[0]][n[1]] # out of bounds else correct
    s = south(i,j)
    s = "0" if s[0] >= len(floor) else floor[s[0]][s[1]] # out of bounds else correct
    nw_ = nw(i,j)
    nw_ = "0" if (nw_[1] < 0 or nw_[0] < 0) else floor[nw_[0]][nw_[1]] # out of bounds else correct
    ne_ = ne(i,j)
    ne_ = "0" if (ne_[1] >= len(floor[0]) or ne_[0] < 0) else floor[ne_[0]][ne_[1]] # out of bounds else correct
    sw_ = sw(i,j)
    sw_ = "0" if (sw_[1] < 0 or sw_[0] >= len(floor)) else floor[sw_[0]][sw_[1]] # out of bounds else correct
    se_ = se(i,j)
    se_ = "0" if (se_[0] >= len(floor) or se_[1] >= len(floor[0])) else floor[se_[0]][se_[1]] # out of bounds else correct

    occupied = len(list(filter(lambda x: x == "#", [n,s,e,w,nw_,ne_,sw_,se_])))
    return occupied

def west(i,j):
    return (i,j-1)
def east(i,j):
    return (i,j+1)
def north(i,j):
    return (i-1,j)
def south(i,j):
    return (i+1,j)
def nw(i,j):
    return (i-1,j-1)
def sw(i,j):
    return (i+1,j-1)
def ne(i,j):
    return (i-1,j+1)
def se(i,j):
    return (i+1,j+1)

def seatscount(fl):
    count = 0
    for line in fl:
        count += len(list(filter(lambda x: x == "#", line)))
    return count


def cycle(fl):
    res = deepcopy(fl)
    for i in range(len(res)):
        for j in range(len(res[i])):
            if fl[i][j] == "L" and checkseat(i,j,fl) == 0:
                res[i][j] = "#"
            elif fl[i][j] == "#" and checkseat(i,j,fl) >= 4:
                res[i][j] = "L"
    return res

# part1
init = floor
count = 0

while True:
    after = cycle(init)
    if after == init:
        print('cycle ends at', count)
        print('silver:', seatscount(after))
        break
    else:
        init = after
        count += 1


def check_in_direction(row, col, direction, fl):
    r_change, c_change = direction
    r = row+r_change
    c = col+c_change

    if not (0<=r< (len(fl)) and 0<=c< (len(fl[0]))): return False
    elif fl[r][c] == "#": return True
    elif fl[r][c] == "L": return False
    else: return check_in_direction(r,c,direction,fl)

def cycle2(fl):
    directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
    res = deepcopy(fl)
    for i in range(len(fl)):
        for j in range(len(fl[i])):
            occ = len(list(filter(lambda x: x == True, [check_in_direction(i,j,direction,fl) for direction in directions])))
            if fl[i][j] == "L" and occ == 0:
                res[i][j] = "#"
            elif fl[i][j] == "#" and occ >= 5:
                res[i][j] = "L"
    return res

# part2
init = floor
count = 0

while True:
    after = cycle2(init)
    if after == init:
        print('cycle ends at', count)
        print('gold:', seatscount(after))
        break
    else:
        init = after
        count += 1
