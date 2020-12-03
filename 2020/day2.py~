f = open("day2.txt").read().splitlines()

# part 1

correct = 0
for t in f:
    a = t.split(" ")[0]         # whole string turned into array for easier processing
    minv = int(a.split("-")[0]) # minimum value
    maxv = int(a.split("-")[1]) # maximum value
    c = t.split(" ")[1][0]      # char to search
    s = t.split(" ")[2]         # string to test
    count = 0
    for ch in s:
        if ch == c:
            count += 1
    if minv <= count and count <= maxv:
            correct += 1

print('silver ' + str(correct))

# part 2

correct = 0
for t in f:
    a = t.split(" ")[0]         # whole string turned into array for easier processing
    pos1 = int(a.split("-")[0]) # 1st position
    pos2 = int(a.split("-")[1]) # 2nd position
    c = t.split(" ")[1][0]      # char to search
    s = t.split(" ")[2]         # string to test
    count = 0
    if s[pos1-1] == c : count += 1
    if s[pos2-1] == c : count += 1
    if count == 1 : correct += 1 # only allow for one match

print('gold ' + str(correct))
