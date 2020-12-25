# improved ver of day17
# slightly more optimized since i don't construct two dictionaries and make multiple deepcopies over each iteration

f = open("day17.txt").read().splitlines()

def cycle(n, world, dimensions):
    space = dict()
    for y, line in enumerate(world):
        for x, c in enumerate(line):
            if dimensions == 3: space[(x,y,0)] = c == '#'
            elif dimensions == 4: space[(x,y,0,0)] = c == '#'

    for turn in range(n):
        num_act_neighbours = dict()
        for coord in space.keys():
            for n in neighbours(coord, dimensions):
                # for each of the neighbours we need to consider, calculate how many neighbours
                # that point has
                num_act_neighbours[n] = num_active_neighbours(n, dimensions, space)

        for k,v in num_act_neighbours.items(): # this is the improved part: i simply add to the master dict instead of making copies
            if space.get(k, False) and not (v == 2 or v == 3): # if active and neighbours are not 2 or 3
                space[k] = False
            elif not space.get(k, False) and v == 3: # if inactive and neighbours are exactly 3
                space[k] = True
        print('turn: {}, actives: {}'.format(turn, sum(space.values())))
    print('star: {}'.format(sum(space.values())))
    print('************\n')

def neighbours(coord, dimensions):
    if dimensions == 3:
        for dx in range(-1,2):
            for dy in range(-1,2):
                for dz in range(-1,2):
                    if dx == dy == dz == 0: continue
                    yield (coord[0] + dx, coord[1] + dy, coord[2] + dz)
    elif dimensions == 4:
        for dx in range(-1,2):
            for dy in range(-1,2):
                for dz in range(-1,2):
                    for dw in range(-1,2):
                        if dx == dy == dz == dw == 0: continue
                        yield (coord[0] + dx, coord[1] + dy, coord[2] + dz, coord[3] + dw)

def num_active_neighbours(coord, dimensions, actives):
    count = 0
    for n in neighbours(coord, dimensions):
        if actives.get(n, False): #if the Value of actives[n] is True
            count += 1
    return count

cycle(6, f, 3)
cycle(6, f, 4)
