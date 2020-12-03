f = list(map(int, open("day1.txt").read().splitlines()))
for i in f:
    for j in f:
        if i + j == 2020:
            print(i*j)
        for k in f:
            if i + j + k == 2020:
                print(i*j*k)
