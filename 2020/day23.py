f = open("day23.txt").read().strip()
cups = []

for idx,c in enumerate(f):
    cups.append(int(c))

def move(cups, part2 = False):
    current = cups[0]
    pick = cups[1:4]
    dest = cups[0] - 1
    while dest in pick or dest == 0:
        if dest == 0:
            dest = max(cups)
        else: dest-=1
    del cups[1:4]
    cups += [cups.pop(0)] # shift current to the end
    pick.reverse()
    for item in pick:
        cups.insert(cups.index(dest)+1, item)

def score_1(cups):
    one_index = cups.index(1)
    res = ''
    for c in cups[one_index+1:] + cups[:one_index]:
         res += str(c)
    print('silver:', res)

# part 1
for i in range(100):
    move(cups)

score_1(cups)

# part 2
cups = []

for idx,c in enumerate(f):
    cups.append(int(c))
cups_init_len = len(cups)
for i in range(1000000-len(cups)):
    cups.append(i+cups_init_len+1)

cups_xs = {} # using a dictionary instead of a real circular linked list :D
for idx, c in enumerate(cups):
    if idx == len(cups)-1: # last value, wrap next back to front to emulate a circle
        cups_xs[c] = cups[0]
    else:
        cups_xs[c] = cups[idx+1]

def move_xs(cups, start, maxval): # set the pointers of the linked list instead of managing indexes of 1 mil elements of a list
    curr_cup = start
    pickup = [next(curr_cup), next(next(curr_cup)), next(next(next(curr_cup)))]
    dest = curr_cup - 1
    while dest in pickup or dest == 0:
        if dest == 0:
            dest = maxval
        else: dest-=1

    dest_next = next(dest) # shifting around the pointers
    cups[dest] = pickup[0]
    cups[curr_cup] = next(pickup[2])
    cups[pickup[2]] = dest_next

    return cups[curr_cup] # returns the next starting cup

def next(cup):
    return cups_xs[cup]

start = int(f[0])
maxval = max(cups)
for i in range(10000000):
    start = move_xs(cups_xs, start, maxval)

print('gold: ', next(1)*next(next(1)))
