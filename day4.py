from collections import defaultdict
def getpass(lowerbound,upperbound):
	size = upperbound - lowerbound + 1
	num = lowerbound
	d = []
	repeat = defaultdict(lambda:1)
	passlist = []
	brokeRule = False
	adjRule = False
	for i in range(size):
		d = [int(m) for m in str(num)]
		for j in range(len(d)):
			if j == 0: 
				continue
			if d[j] < d[j-1]:
				brokeRule = True
			if d[j] == d[j-1]:
				repeat[d[j]] += 1
				adjRule = True
			if j == 5: 
				break
		if((brokeRule != True) and (adjRule == True)):
			print(repeat)
			for k in repeat:
				if repeat[k] == 2:
					passlist.append(num)
					break
		num+=1
		adjRule = False
		brokeRule = False
		repeat.clear()
	return passlist


print(len(getpass(108457,562041)))
#print(getpass(222220,222245))