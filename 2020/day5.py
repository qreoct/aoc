import math

f = open("day5.txt").read().splitlines()

# part 1

def validate_pass(p):
    bot, top = 0, 127
    for char in p[0:6]:
        if char == "F" : top = top - (top-bot+1)//2 # change top boundary
        elif char == "B" : bot = bot + (top-bot+1)//2 # change bottom boundary
    row = bot if p[6] == "F" else top # do the binary stuff then have the last char determine the val

    bot, top = 0, 7
    for char in p[7:9]:
        if char == "R": bot = bot + (top-bot+1)//2  # change bottom boundary
        elif char == "L": top = top - (top-bot+1)//2 # change top boundary 
    col = bot if p[9] == "L" else top # do the binary stuff then have the last char determine the val
    _id = (8 * row) + col
    return(row, col, _id)
        
ids = []
for p in f:
    r, c, i = validate_pass(p)
    ids.append(i)

print("silver:", max(ids))

# part 2
ids = sorted(ids)
for x in range(ids[0], ids[-1]): # your id is the only one not in this range
    if x not in ids: print("gold: ", x)
