f = open("day17.txt").read().splitlines()

from collections import defaultdict
from copy import deepcopy

world = defaultdict(lambda: ".")

# we define (0,0) as the top left of the input

for x, line in enumerate(f):
    for y, c in enumerate(line):
        world[(x,y,0)] = c

def get_active_neighbours(coord, world, dimension):
    if dimension == 3: 
        directions = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    if x == y == z == 0: pass
                    else:
                        directions.append([x,y,z])
    else:
        directions = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    for w in range(-1,2):
                        if x == y == z == w == 0: pass
                        else: 
                            directions.append([x,y,z,w])

    if dimension == 3:
        curr_active = world[coord] == '#'
        active_neighbours = 0
        x,y,z = coord
        for d in directions:
            dx,dy,dz = d
            new_coord = (x+dx, y+dy, z+dz)
            if world[new_coord] == '#': active_neighbours += 1
        return active_neighbours
    else:
        curr_active = world[coord] == '#'
        active_neighbours = 0
        x,y,z,w = coord
        for d in directions:
            dx,dy,dz,dw = d
            new_coord = (x+dx, y+dy, z+dz, w+dw)
            if world[new_coord] == '#': active_neighbours += 1
        return active_neighbours

def get_neighbour_coords(coord, dimension):
    if dimension == 3: 
        directions = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    directions.append([x,y,z])
        x,y,z = coord
        neighbours = []
        for d in directions:
            dx,dy,dz = d
            neighbour_coord = (x+dx, y+dy, z+dz)
            neighbours.append(neighbour_coord)
        return neighbours

    else:
        directions = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    for w in range(-1,2):
                        directions.append([x,y,z,w])

        x,y,z,w = coord
        neighbours = []
        for d in directions:
            dx,dy,dz,dw = d
            neighbour_coord = (x+dx, y+dy, z+dz, w+dw)
            neighbours.append(neighbour_coord)
        return neighbours

def cycle(current_world, dimension):
    new_world = deepcopy(current_world)
    current_coords = [x for x in current_world.keys()]

    coords_to_consider = {}
    for c in current_coords:
        neighbours = get_neighbour_coords(c, dimension)
        for n in neighbours:
            coords_to_consider[n] = 1

    become_inactive = []
    become_active = []

    for coord in coords_to_consider:
        neighbours = get_active_neighbours(coord, new_world, dimension)
        curr_active = current_world[coord] == '#'

        if curr_active and not (neighbours == 2 or neighbours == 3): become_inactive.append(coord) 
        elif neighbours == 3: become_active.append(coord) 

    for c in become_active: new_world[c] = '#'
    for c in become_inactive: new_world[c] = '.'

    return new_world

def count_actives(world):
    return len([x for x in world.values() if x == '#'])

def cycle_for(n, world, dimension):
    working_world = deepcopy(world)
    while n>0:
        working_world = cycle(working_world, dimension)
        print('cycle {}, active {}'.format(n, count_actives(working_world)))
        n-=1
    print('star: ', count_actives(working_world))
    print('fun fact! {} cubes evaluated'.format(len(working_world)))
    print('************\n')

silv_world = deepcopy(world)
cycle_for(6, silv_world, 3)

gold_world = defaultdict(lambda: ".")
for x, line in enumerate(f):
    for y, c in enumerate(line):
        gold_world[(x,y,0,0)] = c
cycle_for(6, gold_world, 4)
