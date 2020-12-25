f = open("day4.txt").read().split("\n\n") #the only consistent splits between each passport is \n\n

# part 1
def is_valid_line(line, part2):
    if part2:
        byr = line.find('byr')
        byr = line[byr+4:byr+8] if line.find('byr') != -1 else '-1'
        iyr = line.find('iyr')
        iyr = line[iyr+4:iyr+8] if line.find('iyr') != -1 else '-1'
        eyr = line.find('eyr')
        eyr = line[eyr+4:eyr+8] if line.find('eyr') != -1 else '-1'
        hcl = line.find('hcl')
        hcl = line[hcl+4:hcl+11] if line.find('hcl') != -1 else '-1'
        ecl = line.find('ecl')
        ecl = line[ecl+4:ecl+7] if line.find('ecl') != -1 else '-1'
        pid = line.find('pid')
        pid = line[pid+4:pid+14].split()[0] if line.find('pid') != -1 else '-1' 
        hgt = line.find('hgt')
        hgt = line[hgt+4:hgt+9] if line.find('hgt') != -1 else '-1' 
    
        valid =  is_valid_byr(byr) and is_valid_iyr(iyr) and is_valid_eyr(eyr) and is_valid_hcl(hcl) and is_valid_ecl(ecl) and is_valid_pid(pid) and is_valid_hgt(hgt)
        return valid
    else:
        return 'ecl' in line and 'pid' in line and 'eyr' in line and 'hcl' in line and 'byr' in line and 'iyr' in line and 'hgt' in line

def is_valid_byr(byr):
    return 1920 <= int(byr) <= 2002

def is_valid_iyr(iyr):
    return 2010 <= int(iyr) <= 2020

def is_valid_eyr(eyr):
    return 2020 <= int(eyr) <= 2030

def is_valid_hcl(hcl):
    return hcl[0] == "#" and len(hcl[1:]) == 6 and all(c in 'abcdef0123456789' for c in hcl[1:])

def is_valid_ecl(ecl):
    return len(ecl) == 3 and ecl in ['amb','blu','brn','gry','grn','hzl','oth']

def is_valid_pid(pid):
    return len(pid) == 9 and all(c in '0123456789' for c in pid)

def is_valid_hgt(hgt):
    if 'in' in hgt : return 59 <= int(hgt.split('in')[0]) <= 76 
    elif 'cm' in hgt : return 150 <= int(hgt.split('cm')[0]) <= 193
    else:  return False

# part 1
count = 0
for line in f:
    if is_valid_line(line, False): count += 1
print("silver: ", count)

# part 2
count = 0
for line in f:
    if is_valid_line(line, True): count += 1
print("gold: ", count)
