f = open("day7.txt").read().splitlines()

def parse(inp): #read the input and get a dict where {"bag": [("contain1",amt), ("contain2",amt)...], ...}
    bags = {}
    for line in inp:
        col = line.split(" bags contain ")[0].replace(" ","")
        if "contain no other" in line: contains = []
        else:
            contains = line.split(" contain ")[1].split(", ")
            res = []
            for c in contains:
                amt = int(c.split(" ")[0].strip())
                color = "".join(c.split(" ")[1:3])
                res.append((color, amt))
            contains = res
        bags[col] = contains
    return bags


def find_gold(bagcol, baglist): # given a starting col, return if you can find gold within
    try:
        found = memo[bagcol] # use memoization to speed up a little
    except:
        contents = baglist[bagcol]
        if len(contents) == 0: return False
        else:
            found = False
            for b in contents:
                found = b[0] == "shinygold" or find_gold(b[0], baglist) or found
            memo[bagcol] = found
            return found

def num_inside_col(col, baglist):
    contents = baglist[col]
    if len(contents) == 0: return 0
    else:
        total = 0
        for b in contents:
            total += b[1]*(num_inside_col(b[0], baglist) + 1)
        return total


# part1
baglist = parse(f)
memo = {'shinygold': False}

part1 = []
for col in baglist:
    part1.append(find_gold(col, baglist))
        
print('silver', part1.count(True))
# part2
print('gold', num_inside_col('shinygold', baglist))
