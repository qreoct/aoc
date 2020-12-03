f = open("day3.txt").read().splitlines()

# part 1

def move(r, d, curr, count):
    if curr[1] >= len(f) : return count
    else:
        x = curr[0] % len(f[0]) if curr[0] >= len(f[0]) else curr[0]
        y = curr[1]
        if f[y][x] == "#" : count += 1
        return move(r,d, (x + r, y + d), count)

print("silver: ", move(3,1,(0,0), 0))

# part 2

a = move(1,1,(0,0), 0)
b = move(3,1,(0,0), 0)
c = move(5,1,(0,0), 0)
d = move(7,1,(0,0), 0)
e = move(1,2,(0,0), 0)
print("gold: ", a*b*c*d*e)
