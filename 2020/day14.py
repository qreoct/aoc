f = open("day14.txt").read().strip().splitlines()

def DecimalToBinary(num):
    if num > 1:
        return DecimalToBinary(num // 2) + str(num%2) 
    else: return str(num)

def BinaryToDecimal(num):
    return int(num, 2)

def pad(num):
    # takes num (as a str datatype) and pads it with zeroes to the left until 36 characters
    for i in range(36-len(num)):
        num = "0"+num
    return num

def apply_mask(mask, num):
    for i in range(len(mask)):
        if mask[i] != 'X':
            # replace char at position
            temp = list(num)
            temp[i] = mask[i]
            num = "".join(temp)
    return BinaryToDecimal(num)

# part1

mem = {}
for line in f:
    if line.split(" ")[0] == "mask":
        mask = line.split(" ")[2].strip()
    else:
        mem_loc = int(line.split("[")[1].split("]")[0])
        mem_val = pad(DecimalToBinary(int(line.split("=")[1].strip())))
        mem[mem_loc] = apply_mask(mask, mem_val)

print('silver: ', sum(mem.values()))

# part2

def apply_mask_2(mask, num):
    for i in range(len(mask)):
        if mask[i] == "0":
            continue
        # replace char at position
        temp = list(num)
        temp[i] = mask[i]
        num = "".join(temp)
    res = list(flatten(replace_X(num)))
    return res

def flatten(L):
    if len(L) == 1:
        if type(L[0]) == list:
            result = flatten(L[0])
        else:
            result = L
    elif type(L[0]) == list:
        result = flatten(L[0]) + flatten(L[1:])
    else:
        result = [L[0]] + flatten(L[1:])
    return result

def replace_X(s):
    # replaces the first instance of "X" in a string with both 0 and 1. returns both in a list, i.e. [replaced_0, replaced_1]
    res = []
    if not 'X' in s: return s
    else:
        for i in range(len(s)):
            if s[i] == "X":
                temp1 = list(s)
                temp2 = list(s)
                temp1[i] = "0"
                temp2[i] = "1"
                res.append(replace_X("".join(temp1)))
                res.append(replace_X("".join(temp2)))
                return res
                break #safety

mem = {}
for line in f:
    if line.split(" ")[0] == "mask":
        mask = line.split(" ")[2].strip()
    else:
        initial_address = pad(DecimalToBinary(int(line.split("[")[1].split("]")[0])))
        value = int(line.split("=")[1].strip())
        ress = apply_mask_2(mask, initial_address)
        for r in ress:
            mem[r] = value #strings are hashable in dicts!

print('gold: ', sum(mem.values()))
