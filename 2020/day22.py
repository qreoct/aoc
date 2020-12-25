f = open("day22.txt").read().split("\n\n")
player1 = list(map(int,f[0].splitlines()[1:]))
player2 = list(map(int,f[1].splitlines()[1:]))


def game(one, two):
    if one[0] > two[0]:
        top = one.pop(0)
        bot = two.pop(0)
        one.append(top)
        one.append(bot)
    else:
        top = two.pop(0)
        bot = one.pop(0)
        two.append(top)
        two.append(bot)

# part1
while not len(player1) == 0 or len(player2) == 0:
    game(player1, player2)

def score_game(deck):
    return sum(val * (len(deck)-idx) for idx, val in enumerate(deck))

print('silver: ', score_game(player1) if len(player2) == 0 else score_game(player2))

from copy import deepcopy

def game_rec(one, two, history):
    if (one, two) in history:
        return 1 # player 1 wins immediately
    elif len(one) == 0:
        return 2
    elif len(two) == 0:
        return 1
    elif len(one[1:]) >= one[0] and len(two[1:]) >= two[0]:
        res = game_rec(deepcopy(one[1:one[0]]), deepcopy(two[1:two[0]]), [])
        history.append(( deepcopy(one), deepcopy(two) ))
        if res == 1:
            top = one.pop(0) # see line 74 for neater way
            bot = two.pop(0)
            one.append(top)
            one.append(bot)
        else:
            top = two.pop(0)
            bot = one.pop(0)
            two.append(top)
            two.append(bot)
        return game_rec(one, two, history) 
    else:
        history.append((deepcopy(one), deepcopy(two)))
        if one[0] > two[0]:
            top = one.pop(0)
            bot = two.pop(0)
            one.append(top)
            one.append(bot)
        else:
            top = two.pop(0)
            bot = one.pop(0)
            two.append(top)
            two.append(bot)
        return game_rec(one, two, history) 

def game_rec2(one, two):
    history = set()
    while one and two:
        if (tuple(one), tuple(two)) in history: return 1 # player 1 wins immediately
        history.add((tuple(one),tuple(two)))
        if one[0] <= len(one[1:]) and two[0] <= len(two[1:]):
            res = game_rec2(one[1:one[0]+1], two[1:two[0]+1]) # OFF BY ONE HAPPENED HERE!
            if res == 1:
                one += [one.pop(0), two.pop(0)]
            elif res == 2:
                two += [two.pop(0), one.pop(0)]
        elif one[0]>two[0]:
            one += [one.pop(0), two.pop(0)]
        else:
            two += [two.pop(0), one.pop(0)]
    if one:
        return 1
    elif two:
        return 2

player1 = list(map(int,f[0].splitlines()[1:]))
player2 = list(map(int,f[1].splitlines()[1:]))
res = game_rec2(player1, player2)
print('gold: ', score_game(player1) if res == 1 else score_game(player2))

