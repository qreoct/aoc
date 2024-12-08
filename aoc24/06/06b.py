from collections import defaultdict
import copy
from itertools import combinations

"""
absolutely disgusting brute force method

initially, i thought i could come up with a clever
thing by observing that given this configuration:

...b....
...|--c.
..a|....
...|....

where a, b, c are obstacles and you start traveling
from the bottom (i.e. hit b, then c), then the property
of b is that it is a 'pivot' (i.e. abs(b.y - c.y) = 1 and
abs(b.x - a.x) = 1), and it would be possible to
calculate the coordinates where d should be in order
to get a loop.

BUT. turns out loops are not simply a single loop.
there may be multi loops (see Option 5 in the problem
statement).

so i just brute force by trying to place the new obstacle
in every potential location.
"""

start = (0,0)
position = (0,0)
obstacles = defaultdict(lambda: 0)
visited = defaultdict(lambda: 0)
direction = (0,-1)
width = 0
height = 0

def change_direction(direction):
    return (-direction[1], direction[0])

with open('../in/06a.txt') as f:
    y = 0
    for line in f.readlines():
        for x, c in enumerate(line):
            if c == '#':
                obstacles[(x, y)] += 1
            elif c == '^':
                start = (x,y)
                position = (x,y)
        width = x
        y += 1
    height = y

f.close()

#print(f"obstacles keys: {obstacles.keys()}")
print(f"pos: {position}, width: {width}, height: {height}")

in_bounds = True

def generate_possible_new_obstacles():
    """
    while traveling through the grid, just take note of all spots
    where the new obstacle could be.
    """
    position = start
    in_bounds = True
    new_obstacles = []
    direction = (0,-1)
    while in_bounds:
        if position[0] < 0 or position[1] < 0 or position[0] > width or position[1] > height:
            in_bounds = False
            return new_obstacles
        visited[(position[0], position[1])] += 1
        nxt = (position[0]+direction[0], position[1]+direction[1])
        if obstacles.get(nxt, 0) > 0:
            direction = change_direction(direction)
        else:
            position = nxt
            if nxt != start and nxt[0] >= 0 and nxt[1] >= 0: new_obstacles.append(nxt)

def traverse(start, new_obstacle):
    """
    traverse the grid. returns False if the guard manages to escape
    returns True if the guard gets stuck in a loop (i.e. at any point if visited >= 10)

    just for fun, the normal traverse only will at most visit a point 4 times
    """
    position = start
    in_bounds = True
    direction = (0,-1)
    visited_new = copy.deepcopy(visited)
    obstacles_new = copy.deepcopy(obstacles)
    obstacles_new[new_obstacle] += 1
    for k in visited.keys():
        visited_new[k] = 0

    while in_bounds:
        if position[0] < 0 or position[1] < 0 or position[0] > width or position[1] > height:
            in_bounds = False
            return False
        visited_new[(position[0], position[1])] += 1
        if visited_new[(position[0], position[1])] >= 10:
            return True
        nxt = (position[0]+direction[0], position[1]+direction[1])
        if obstacles_new.get(nxt, 0) > 0:
            direction = change_direction(direction)
        else:
            position = nxt
    pass

# while in_bounds:
#     if position[0] < 0 or position[1] < 0 or position[0] > width or position[1] > height:
#         in_bounds = False
#         break
#     visited[(position[0], position[1])] += 1
#     nxt = (position[0]+direction[0], position[1]+direction[1])
#     if obstacles.get(nxt, 0) > 0:
#         direction = change_direction(direction)
#     else:
#         position = nxt

# def calc_mirror(pivot, two, three):
#     y_diff = two[1] - pivot[1]
#     x_diff = two[0] - pivot[0]
#     new = (three[0] + x_diff, three[1] + y_diff)
#     return new

def print_grid(width, height, path, obstacles):
    for j in range(width):
        for i in range(height):
            if (i,j) in obstacles:
                print('#', end='')
            elif (i,j) == start:
                print('$', end='')
            elif (i,j) in path:
                print('x', end='')
            else:
                print('.', end='')
        print('\n')

#print_grid(width, height, [], obstacles.keys())

new_obstacles = set(generate_possible_new_obstacles())
print(f"new obstacles: {new_obstacles}")

res = 0
for o in new_obstacles:
    print("---\n")
    if traverse(start, o):
        res += 1
        print(f"we can place at {o}")

print(len(visited.values()))
print(max(visited.values()))
print(f"part 2: { res }")


