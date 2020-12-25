f = open("day24.txt").read().splitlines()

dirs = {
    "nw": ( 0, 1,-1),
    "ne": (+1, 0,-1),
    "e" : (+1,-1, 0),
    "se": ( 0,-1,+1),
    "sw": (-1, 0,+1),
    "w" : (-1, 1, 0)
}

from collections import defaultdict
changed_tiles = defaultdict(lambda: True) # true is white

for instr in f:
    line = instr
    changed_tile = (0,0,0)
    while line:
        x,y,z = changed_tile
        if line[0:2] in ["nw", "ne", "sw", "se"]:
            dx,dy,dz = dirs[line[0:2]]
            changed_tile = (x+dx, y+dy, z+dz)
            line = line[2:]
        else:
            dx,dy,dz = dirs[line[0]]
            changed_tile = (x+dx, y+dy, z+dz)
            line = line[1:]

    changed_tiles[changed_tile] = not changed_tiles[changed_tile]

print('silver: ', len([x for x in changed_tiles.values() if x == False]))

black_tiles = set(x for x in changed_tiles.keys() if changed_tiles[x] == False)

def num_black_neighbours(tile):
    x,y,z = tile
    count = 0
    for dir in dirs.values():
        dx, dy, dz = dir
        if (x+dx, y+dy, z+dz) in black_tiles: count += 1
    return count

def neighbour_tiles(tile):
    x,y,z = tile
    neighbours = []
    for dir in dirs.values():
        dx, dy, dz = dir
        neighbours.append((x+dx, y+dy, z+dz))
    return neighbours

def cycle(n, black_tiles):
    for turn in range(n):
        tiles_to_consider = set()
        flip_to_white = set()
        flip_to_black = set()

        for t in black_tiles:
            for n in neighbour_tiles(t):
                tiles_to_consider.add(n)
            tiles_to_consider.add(t)

        for tile in tiles_to_consider:
            if tile in black_tiles and (num_black_neighbours(tile) == 0 or num_black_neighbours(tile) > 2):
                flip_to_white.add(tile)
            elif tile not in black_tiles and num_black_neighbours(tile) == 2:
                flip_to_black.add(tile)

        for tile in flip_to_white:
            black_tiles.remove(tile)
        for tile in flip_to_black:
            black_tiles.add(tile)

    return black_tiles

print('gold: ', len(cycle(100, black_tiles)))


