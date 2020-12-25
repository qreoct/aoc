f = open("day21.txt").read().splitlines()

from collections import defaultdict
ingredients = {}
allergens = defaultdict(list) 
total_allergens = set() 
total_ingredients = set()
for i in f:
    ingr = i.split('(')[0].strip().split(' ')
    alls = i.split('contains ')[1].replace(')', '').replace(' ','').split(',')
    for a in alls:
        allergens[a].append(ingr)
        total_allergens.add(a)

real_allergens = set() 
for key, a in allergens.items():
    real_allergic = set.intersection(*[set(x) for x in a])
    print('****** {} {}'.format(key, real_allergic))
    for item in real_allergic:
        real_allergens.add(item)
    ingredients[key] = real_allergic

diff = set.difference(total_ingredients, real_allergens)
print('real allergens', real_allergens)

silver = 0
for line in f:
    l = set(line.split('(')[0].strip().split(' '))
    silver += len(l-real_allergens) # get the set difference
print('silver: ', silver)


while not sum(len(s) for s in ingredients.values()) == len(real_allergens): # while the allergens list does not all have length 1 
    for s in ingredients.values():
        if len(s) == 1:
            for key, v in ingredients.items():
                if len(v) != 1:
                    ingredients[key] = v - s

gold = [] 
for i in sorted(ingredients):
    gold.append(ingredients[i].pop())

print('gold:', ','.join(gold))
