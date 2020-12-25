from itertools import product

f = open("day19.txt").read().split('\n\n')
rules = {}
for rule in f[0].splitlines():
    key, val = rule.split(": ")
    rules[int(key)] = val.replace('"','')

def simplify_pattern(rulelist, idx):
    val = rulelist[idx]
    if not any(c.isdigit() for c in val):
        yield val
    else:
        variations = val.split(' | ')
        for v in variations:
            res = [simplify_pattern(rulelist, int(i)) for i in v.split(' ')] # recursively get the strings which match the inner patterns
            combinations = product(*res) # then cartesian product together. e.g. 3: "a" 4: "b" 0: 3 4 | 4 3 so combinations is a generator of [ a b, b a ]
            # in larger examples, cartesian product of rule 3 and 4 will include all possibilities for rule 3 and 4, if they are large
            for combi in combinations:
                yield ''.join(combi)

patterns = [p for p in simplify_pattern(rules, 0)]

silv = []
for pat in f[1].splitlines():
    silv.append(pat in patterns) 
print('silver:', sum(silv))

