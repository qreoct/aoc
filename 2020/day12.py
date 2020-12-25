f = open("day12.txt").read().splitlines()

def move(dir, pos, insts, waypoint_enabled, waypt):
    directions = ['N','E','S','W']
    if insts == []: return pos
    else:
        command = insts[0][0]
        amt = int(insts[0][1:])
        if command == "R":
            if waypoint_enabled:
                newwaypt = turn("R", amt, waypt)
                return move(dir, pos, insts[1:], waypoint_enabled, newwaypt)
            else:
                dir = (dir+(amt//90))%4
                return move(dir, pos, insts[1:], waypoint_enabled, waypt)
        elif command == "L":
            if waypoint_enabled:
                newwaypt = turn("L", amt, waypt)
                return move(dir, pos, insts[1:], waypoint_enabled, newwaypt)
            else:
                dir = (dir-(amt//90))%4
                return move(dir, pos, insts[1:], waypoint_enabled, waypt)
        elif command == "E":
            if waypoint_enabled:
                x,y = waypt
                return move(dir, pos, insts[1:], waypoint_enabled, [x+amt, y])
            else:
                x,y = pos
                return move(dir, [x+amt,y], insts[1:], waypoint_enabled, waypt)
        elif command == "W":
            if waypoint_enabled:
                x,y = waypt
                return move(dir, pos, insts[1:], waypoint_enabled, [x-amt, y])
            else:
                x,y = pos
                return move(dir, [x-amt,y], insts[1:], waypoint_enabled, waypt)
        elif command == "N":
            if waypoint_enabled:
                x,y = waypt
                return move(dir, pos, insts[1:], waypoint_enabled, [x, y+amt])
            else:
                x,y = pos
                return move(dir, [x, y+amt], insts[1:], waypoint_enabled, waypt)
        elif command == "S":
            if waypoint_enabled:
                x,y = waypt
                return move(dir, pos, insts[1:], waypoint_enabled, [x, y-amt])
            else:
                x,y = pos
                return move(dir, [x, y-amt], insts[1:], waypoint_enabled, waypt)
        elif command == "F":
            if waypoint_enabled:
                x,y = pos
                return move(dir, [x+amt*waypt[0], y+amt*waypt[1]], insts[1:], waypoint_enabled, waypt)
            else:
                changedir = insts
                changedir.remove(changedir[0])
                changedir.insert(0, directions[dir]+str(amt))
                return move(dir, pos, changedir, waypoint_enabled, waypt)
        else: print("error at", dir, pos, insts)

from math import cos, sin, radians

def turn(dir, angle, waypt):
    w_x, w_y = waypt
    if dir == "L": #anticlockwise, using rotation matrix
        new_x = round(w_x*cos(radians(angle)) - w_y*sin(radians(angle)))
        new_y = round(w_x*sin(radians(angle)) + w_y*cos(radians(angle)))
        return [new_x, new_y]
    elif dir == "R": #clockwise, using rotation matrix
        new_x = round(w_x*cos(radians(angle)) + w_y*sin(radians(angle)))
        new_y = round(-w_x*sin(radians(angle)) + w_y*cos(radians(angle)))
        return [new_x, new_y]

import copy
f_silver = copy.deepcopy(f)
x,y = move(1,[0,0],f_silver, False, [0,0])
print('silver:', abs(x)+abs(y))

f_gold = copy.deepcopy(f)
x,y = move(1,[0,0],f_gold, True, [10,1]) #waypoint starts 10 E, 1 N
print('gold:', abs(x)+abs(y))
