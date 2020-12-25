f = open("day6.txt").read().split('\n\n')

silver = 0
for group in f:
    group_answers = set()
    groups = group.splitlines()
    for person in groups:
        for c in person:
            group_answers.add(c)
    silver += len(group_answers)

print('silver:', silver)

gold = 0
for group in f:
    groups = group.splitlines()
    group_answers = []
    for person in groups:
        person_answers = set()
        for c in person:
            person_answers.add(c)
        group_answers.append(person_answers)
    gold += len(set.intersection(*group_answers))

print('gold:', gold)


