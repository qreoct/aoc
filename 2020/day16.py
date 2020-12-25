f = open("day16.txt").read().strip().split("\n\n")

rules = f[0].split('\n')
mine = list(map(int, f[1].split('\n')[1].split(',')))
nearby = f[2].split('\n')[1:]

rule_array = [] # turns the rules into an array [ [[min1,max1],[min2,max2]], ... ] for each rule
for rule in rules:
    rnge = rule.split(": ")[1].split(" or ")
    res = []
    for r in rnge:
        res.append(list(map(int, r.split('-'))))
    rule_array.append(res)

invalid = 0 # calculate the invalid number
valids = [] # get an array of only valid nearby for part2

def pass_rule(c, rule):
    r1_min = rule[0][0]
    r1_max = rule[0][1]
    r2_min = rule[1][0]
    r2_max = rule[1][1]
    return (r1_min <= c <= r1_max or r2_min <= c <= r2_max)

# part 1 =============================================================
for n in nearby: # pretty much bruteforce. check each nearby if it passes each rule
    check = n.split(",")
    ticket_valid = True
    for c in check:
        c = int(c)
        in_range = False
        for rule in rule_array:
            if in_range: break
            in_range = in_range or pass_rule(c, rule)
        if not in_range:
            invalid += c
            ticket_valid = False
    if ticket_valid: 
            valids.append(n)
print('silver', invalid)
# ====================================================================

# part2
mat = []

for v in valids: 
    #build an array such that for each nearby, have a list of truth values such that 
    #we know which index passes which rule
    #i.e. if there are 4 rules, then a result could be [True,True,False,True, True,False,False,False, False,True,True,True, False,False,False,True]
    #so we know that eg at index 1, it only fulfills rule 1, at index 3, it only fulfills rule 4
    res = []
    for c in v.split(','):
        c = int(c)
        for rule in rule_array:
            res.append(pass_rule(c, rule))
    mat.append(res)

corrects = [[x for x in range(len(rule_array))] for y in range(len(rule_array))]

for truths in mat:
    #now, for each of the 'truths' in this list, we can guarantee that the False values do not meet the rules, so we can remove it
    for i, elem in enumerate(truths):
        if elem == False:
            pos = i//(len(rule_array))
            corrects[pos].remove(i%(len(rule_array)))

def remove_from_list(c, xs): #helper function to destructively remove items
    if len(xs) == 1: pass
    else: 
        try:
            xs.remove(c) 
        except:
            pass

def clean():
    for c in corrects:
        if len(c) == 1: 
            for subl in corrects: remove_from_list(c[0], subl)
for i in range(15): clean() #okay i know this is really really ugly but i think recursively reducing until everything is len(1) is probably LESS optimal...

gold = 1
for pos, i in enumerate(corrects):
    if 0 <= i[0] <= 5:
        gold *= mine[pos]
print('gold:', gold)
