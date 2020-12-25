door_pub, card_pub = list(map(int,open("day25.txt").read().splitlines()))

def transform(n, subject):
    val = 1
    for i in range(n):
        val *= subject
        val = val % 20201227
    return val

def untransform(target, subject):
    i = 0
    res = 1
    while not res == target:
        res *= subject
        res = res % 20201227
        i += 1
    return i

door_loop = untransform(door_pub, 7)
card_loop = untransform(card_pub, 7)

print('door: {}, card: {}'.format(door_loop, card_loop))
print('silver: ', transform(card_loop, door_pub), transform(door_loop, card_pub))
