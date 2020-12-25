f = open("day20.txt").read().split('\n\n')

class Tile(object):
    def __init__(self, data):
        self.data = data
        self.edges = []
        self.numNeighbours = 0
        self.neighbours = []
        self.art = []
    def __str__(self):
        return 'Tile {}: EDGES {}, NUMNEIGHBOURS {}, NEIGHBOURS {}'.format(self.data,self.edges,self.numNeighbours,self.neighbours)
    def getName(self):
        return self.data
    def getEdges(self):
        return self.edges
    def getNeighbours(self):
        return self.neighbours
    def setNeighbour(self, neighbour):
        if neighbour not in self.neighbours:
          self.neighbours.append(neighbour)
    def setEdges(self, edges):
        self.edges = edges
    def setnumNeighbours(self, num):
        self.numNeighbours = num
    def setArt(self, art):
        self.art = art

tiles = {}
for tile in f:
    tilenum = tile.splitlines()[0].split(' ')[1].strip(':')
    tileheight = len(tile.splitlines())
    edge1 = tile.splitlines()[1]
    edge2 = ''.join(tile.splitlines()[i][0] for i in range(1,tileheight))
    edge3 = tile.splitlines()[-1]
    edge4 = ''.join(tile.splitlines()[i][-1] for i in range(1,tileheight))
    ART = tile.splitlines()[1:]
    ART = ART[1:-1]
    for idx, line in enumerate(ART):
        ART[idx] = line[1:-1]

    tiles[tilenum] = Tile(tilenum)
    tiles[tilenum].setArt(ART)
    tiles[tilenum].setEdges([edge1,edge2,edge3,edge4])

def num_edges(tile): # hacky way. we don't even arrange the tiles, just get the ones with exactly 2 neighbour tiles.
    count = 0
    for edge in tiles[tile].edges:
        for t in tiles.keys():
            if t == tile: continue
            elif edge in tiles[t].edges or edge[::-1] in tiles[t].edges:
                count += 1
                tiles[tile].setNeighbour(t) 
    tiles[tile].setnumNeighbours(count)
    return count

def count_hash(art):
    count = 0
    for line in art:
        for c in line:
            if c == '#': count += 1
    return count

silver = 1
for t in tiles.keys():
    if num_edges(t) == 2:
        silver *= int(t)
print('silver:', silver)

hashes = 0
for tile in tiles.values():
    hashes += count_hash(tile.art)
print('total hashes:', hashes) # mm.... may have just guessed the number of monsters that exist. maybe a proper solution will appear one day
